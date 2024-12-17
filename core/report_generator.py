import os
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet

parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
REPORTS_FOLDER = os.path.join(parent_dir, "reports")
SCREENSHOTS_FOLDER = os.path.join(REPORTS_FOLDER, "screenshots")

os.makedirs(SCREENSHOTS_FOLDER, exist_ok=True)


def generate_pdf_report_single(test_name, result, details, screenshot_path=None):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pdf_path = os.path.join(REPORTS_FOLDER, f"test_report_{timestamp}.pdf")

    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title = Paragraph("Test Report", title_style)
    elements.append(title)

    data = [
        ["Step", "Action", "Result", "Screenshot"]
    ]

    screenshot = ""
    if screenshot_path and os.path.exists(screenshot_path):
        screenshot = Image(screenshot_path, width=128, height=80)

    data.append([str(1), details, result, screenshot])

    table = Table(data)
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
    ]))

    elements.append(table)

    doc.build(elements)

    print(f"PDF report saved: {pdf_path}")