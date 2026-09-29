from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

ROOT = Path(__file__).resolve().parents[1]
src = ROOT / "report" / "UniBoard_Assignment1.md"
out = ROOT / "report" / "UniBoard_Assignment1.pdf"
text = src.read_text(encoding="utf-8")
styles = getSampleStyleSheet()
story = []
for raw in text.splitlines():
    line = raw.strip()
    if not line:
        story.append(Spacer(1, 5))
    elif line.startswith("# "):
        story.append(Paragraph(line[2:], styles["Title"]))
    elif line.startswith("## "):
        story.append(Paragraph(line[3:], styles["Heading1"]))
    elif line.startswith("### "):
        story.append(Paragraph(line[4:], styles["Heading2"]))
    else:
        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        story.append(Paragraph(safe.replace("**", ""), styles["BodyText"]))
        story.append(Spacer(1, 3))
SimpleDocTemplate(str(out), pagesize=A4, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=42).build(story)
print(out)