"""Convert the course PDFs to Markdown for the exam knowledge base.

docling inlines page-bottom footnotes into the body (splicing legal citations into
the middle of sentences) and also misclassifies/drops many of them. We instead get
the complete footnote set straight from the PDF text layer (extract_footnotes), use
it to (a) remove footnote lines from the body by content match — which correctly
leaves legitimate body mentions of a case alone — and (b) write a per-module
"<stem>.footnotes.json" sidecar that split_corpus.py re-attaches as a "## Footnotes"
section at the end of each module.

Usage:
    python convert_pdfs.py "STEP Advanced Certificate in Company Law and Practice"
"""
import html
import json
import re
import sys
from pathlib import Path

from docling.document_converter import DocumentConverter

from extract_footnotes import extract_footnotes
from text_cleanup import clean_markdown


def _signature(text: str) -> str:
    """Normalised prefix used to match a footnote against a body line."""
    return re.sub(r"[^a-z0-9]", "", text.lower())[:40]


def doc_to_markdown(doc, footnotes: dict[str, list[str]]) -> str:
    """Body markdown with footnote lines removed (matched against the text-layer
    footnotes, so a footnote dumped inline is removed while a legitimate body
    sentence that merely names the same case is kept)."""
    md = doc.export_to_markdown()
    if footnotes:
        sigs = {_signature(t) for texts in footnotes.values() for t in texts}
        kept = []
        for line in md.split("\n"):
            s = _signature(html.unescape(line.strip()))
            if len(s) >= 20 and s in sigs:
                continue
            kept.append(line)
        md = re.sub(r"\n{3,}", "\n\n", "\n".join(kept))
    return clean_markdown(md)


if __name__ == "__main__":
    ROOT = Path(__file__).parent
    subfolder = sys.argv[1] if len(sys.argv) > 1 else ""
    MATERIALS = ROOT / "Materials" / subfolder if subfolder else ROOT / "Materials"
    OUTPUT = ROOT / "Markdown" / subfolder if subfolder else ROOT / "Markdown"
    OUTPUT.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(MATERIALS.glob("*.pdf"))
    if not pdfs:
        print(f"No PDF files found in {MATERIALS}")
        sys.exit(1)

    converter = DocumentConverter()
    for pdf in pdfs:
        print(f"Converting {pdf.name} ...")
        # Footnote handling is specific to the multi-module Course Manual.
        footnotes = extract_footnotes(pdf) if "Course Manual" in pdf.stem else {}
        md = doc_to_markdown(converter.convert(pdf).document, footnotes)
        (OUTPUT / (pdf.stem + ".md")).write_text(md)
        fn_path = OUTPUT / (pdf.stem + ".footnotes.json")
        if footnotes:
            fn_path.write_text(json.dumps(footnotes, ensure_ascii=False, indent=0))
            print(f"  -> {pdf.stem}.md  (+{sum(len(v) for v in footnotes.values())} footnotes)")
        else:
            if fn_path.exists():
                fn_path.unlink()
            print(f"  -> {pdf.stem}.md")
    print("Done.")
