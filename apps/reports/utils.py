from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def build_basic_report(title, lines):
    buffer = BytesIO()
    page = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 72
    page.setFont("Helvetica-Bold", 16)
    page.drawString(72, y, title)
    page.setFont("Helvetica", 11)
    y -= 36
    for line in lines:
        page.drawString(72, y, line)
        y -= 18
    page.showPage()
    page.save()
    buffer.seek(0)
    return buffer
