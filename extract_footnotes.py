"""Extract footnotes directly from a PDF's text layer (pypdfium2).

docling's layout model misclassifies/drops ~70 of this manual's footnotes. The PDF
is digital (clean text layer) and footnotes are reliably distinguishable: they sit
in a smaller font at the bottom of the page and are numbered sequentially.

Strategy:
  * use per-glyph boxes only to locate the footnote REGION (the small-font band
    below the body) — coordinates, not text, so descenders/order don't matter;
  * extract that region's text with get_text_bounded(), which renders clean text
    (correct descenders, spaces and line order);
  * parse footnotes with a resilient running counter (rejects stray numbers like a
    wrapped year, resyncs over the odd missing number), mapping each to its module
    via the page's running header.

Footnote numbering is exam-specific: Company Law runs 1-111 then restarts at Module 6
and runs 1-236; Trusts runs 1-350 straight through. The restart is detected (a "1."
seen while deep into the count), not hardcoded, so both work without configuration.

API:
    extract_footnotes(pdf_path) -> dict[str, list[str]]   # {module_number: [texts]}
"""
import re
import statistics

import pypdfium2 as pdfium

_MODULE_HEADER = re.compile(r"Module (\d+):")
_FN_START = re.compile(r"^(\d+)\s*\.\s*")
_WINDOW = 8                      # counter tolerance for skips / stray numbers


def _page_lines(page):
    """Rough line reconstruction for height/position stats only (text may carry
    minor descender artifacts — clean text comes from get_text_bounded later).
    Returns [(y_bottom, y_top, median_height, text), ...] top-to-bottom."""
    tp = page.get_textpage()
    items, last_b = [], None
    for i in range(tp.count_chars()):
        ch = tp.get_text_range(i, 1)
        if ch in ("\r", "\n"):
            continue
        try:
            l, b, r, t = tp.get_charbox(i)
            h = t - b
        except Exception:
            l, b, h = 0, (last_b or 0), 0
        if ch == " " and last_b is not None:
            b = last_b
        items.append((b, l, ch, h))
        if ch.strip():
            last_b = b
    items.sort(key=lambda c: (-c[0], c[1]))
    groups, cur, cy = [], [], None
    for it in items:
        # tolerance 4.5 keeps descenders (g, y, j, p) on their own line instead of
        # splitting into phantom lines with spuriously large heights.
        if cy is None or abs(it[0] - cy) <= 4.5:
            cur.append(it)
            cy = it[0] if cy is None else cy
        else:
            groups.append(cur)
            cur, cy = [it], it[0]
    if cur:
        groups.append(cur)
    out = []
    for g in groups:
        g.sort(key=lambda c: c[1])
        text = "".join(c[2] for c in g)
        hs = sorted(c[3] for c in g if c[3] > 0 and c[2].strip())
        med = hs[len(hs) // 2] if hs else 0.0
        out.append((min(c[0] for c in g), max(c[0] + c[3] for c in g), round(med, 2), text))
    return out


def _body_height(doc) -> float:
    meds = [h for pno in range(len(doc))
            for (_yb, _yt, h, txt) in _page_lines(doc[pno]) if len(txt) > 30 and h > 0]
    return statistics.median(meds) if meds else 5.3


def _is_furniture(text: str) -> bool:
    t = text.strip()
    # A numbered footnote may itself cite a module or another STEP certificate, so
    # the leading number wins over the running-header patterns below.
    if _FN_START.match(t):
        return False
    return bool(_MODULE_HEADER.search(t)) or "STEP Advanced Certificate" in t \
        or bool(re.fullmatch(r"\d{1,3}", t))


def _normalise(text: str) -> str:
    m = _FN_START.match(text)
    return f"{m.group(1)}. " + text[m.end():].strip() if m else text


def extract_footnotes(pdf_path) -> dict[str, list[str]]:
    doc = pdfium.PdfDocument(str(pdf_path))
    small_max = _body_height(doc) * 0.9     # footnote lines are smaller than body

    by_module: dict[str, list[str]] = {}
    module = None
    expected = 1

    current = None
    current_module = None

    def flush():
        nonlocal current
        if current is not None and not re.fullmatch(r"\d+\.", current.strip()):
            by_module.setdefault(str(current_module), []).append(current.strip())
        current = None

    for pno in range(len(doc)):
        page = doc[pno]
        tp = page.get_textpage()
        w, ph = page.get_size()
        lines = _page_lines(page)

        # module from the running header (topmost lines)
        for (_yb, _yt, _h, txt) in lines[:3]:
            m = _MODULE_HEADER.search(txt)
            if m:
                module = int(m.group(1))
                break
        # Footnote lines are the small-font, non-furniture lines (the small-font
        # filter excludes body text and the tall descender-phantom artifacts). Get
        # each line's clean text from a thin get_text_bounded band (no body bleeds
        # in) and assemble footnotes with a resilient running counter.
        for (yb, yt, h, rough) in lines:        # top-to-bottom
            if not (0 < h <= small_max) or _is_furniture(rough):
                continue
            clean = tp.get_text_bounded(left=0, bottom=yb - 1, right=w, top=yt + 1)
            clean = re.sub(r"\s+", " ", clean.replace("\r\n", " ")).strip()
            if not clean or _is_furniture(clean):
                continue
            m = _FN_START.match(clean)
            n = int(m.group(1)) if m else None
            # Numbering may restart part-way through the manual (Company Law resets
            # at Module 6; Trusts runs 1-350 straight through), so detect the restart
            # -- a "1." while deep into the count -- instead of hardcoding a module.
            if n == 1 and expected > 20:
                flush()
                expected = 1
            if m and expected <= n <= expected + _WINDOW:
                flush()
                current = _normalise(clean)
                current_module = module
                expected = int(m.group(1)) + 1
            elif current is not None:
                current += " " + clean
        flush()        # footnotes don't span pages -> close at page end
    flush()
    doc.close()
    return by_module


if __name__ == "__main__":
    import sys
    from pathlib import Path
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "Materials/STEP Advanced Certificate in Company Law and Practice/Course Manual.pdf")
    fns = extract_footnotes(pdf)
    total = 0
    for mod in sorted(fns, key=int):
        nums = [int(re.match(r"^(\d+)\.", t).group(1)) for t in fns[mod] if re.match(r"^\d+\.", t)]
        rng = f"{min(nums)}-{max(nums)}" if nums else "-"
        gaps = [n for n in range(min(nums), max(nums) + 1) if n not in set(nums)] if nums else []
        total += len(fns[mod])
        print(f"Module {mod:>2}: {len(fns[mod])} footnotes, range {rng}, gaps {gaps}")
    print("TOTAL footnotes:", total)
