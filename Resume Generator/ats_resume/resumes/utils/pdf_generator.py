from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from django.conf import settings

BASE_DIR = settings.BASE_DIR


def generate_resume_pdf(resume):
    file_path = f"media/resume_{resume.id}.pdf"
    pdf = canvas.Canvas(file_path, pagesize=A4)
    text = pdf.beginText(40, 800)

    text.setFont("Helvetica", 11)

    text.textLine(resume.name.upper())
    text.textLine(resume.email)
    text.textLine("")

    text.textLine("SKILLS")
    text.textLine(resume.skills)
    text.textLine("")

    text.textLine("EXPERIENCE")
    text.textLine(resume.experience)
    text.textLine("")

    text.textLine("EDUCATION")
    text.textLine(resume.education)

    pdf.drawText(text)
    pdf.save()
    return file_path
MEDIA_ROOT = BASE_DIR / 'media'