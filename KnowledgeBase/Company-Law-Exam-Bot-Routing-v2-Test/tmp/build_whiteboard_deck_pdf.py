from pathlib import Path

from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


ROOT = Path("/Users/michaelshieh/Desktop/Claude Projects/STEP Exam/KnowledgeBase/Company-Law-Exam-Bot-Routing-v2-Test")
SLIDES = ROOT / "output" / "whiteboard-routing-v2-q1"
OUTPUT = ROOT / "output" / "pdf" / "Routing-v2-Q1-Whiteboard-Deck.pdf"

# 16:9 landscape. Images are 1672x941, so this page shape needs no cropping.
PAGE_WIDTH = 960
PAGE_HEIGHT = 540


def main() -> None:
    images = [SLIDES / f"slide-{index:02d}.png" for index in range(1, 26)]
    missing = [path.name for path in images if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing slides: {missing}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(OUTPUT), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    pdf.setTitle("Routing v2 Question 1 Whiteboard Deck")
    pdf.setSubject("25-slide Cantonese whiteboard presentation")
    pdf.setAuthor("Codex")

    for image_path in images:
        image = ImageReader(str(image_path))
        width, height = image.getSize()
        if width / height < 1.77 or width / height > 1.79:
            raise ValueError(f"Unexpected slide aspect ratio: {image_path.name} ({width}x{height})")
        pdf.drawImage(image, 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT, mask="auto")
        pdf.showPage()

    pdf.save()
    print(OUTPUT)


if __name__ == "__main__":
    main()
