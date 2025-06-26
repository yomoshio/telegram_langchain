from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether
from reportlab.lib.units import inch
from reportlab.lib import colors
import markdown
from bs4 import BeautifulSoup
import os
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


styles = getSampleStyleSheet()


if 'Title' not in styles:
    styles.add(ParagraphStyle(name='Title', fontSize=22, leading=26, spaceAfter=18, fontName='Helvetica-Bold', textColor=colors.navy, alignment=1))
if 'Heading1' not in styles:
    styles.add(ParagraphStyle(name='Heading1', fontSize=18, leading=22, spaceAfter=14, fontName='Helvetica-Bold', textColor=colors.darkblue, backColor=colors.lightgrey))
if 'Heading2' not in styles:
    styles.add(ParagraphStyle(name='Heading2', fontSize=14, leading=18, spaceAfter=10, fontName='Helvetica-Bold', textColor=colors.darkblue))
if 'BodyText' not in styles:
    styles.add(ParagraphStyle(name='BodyText', fontSize=11, leading=15, spaceAfter=12, fontName='Helvetica', textColor=colors.black))
if 'Bullet' not in styles:
    styles.add(ParagraphStyle(name='Bullet', fontSize=11, leading=15, leftIndent=40, bulletIndent=20, spaceAfter=8, fontName='Helvetica', textColor=colors.black))
if 'TableText' not in styles:
    styles.add(ParagraphStyle(name='TableText', fontSize=10, leading=12, fontName='Helvetica', textColor=colors.black))

def markdown_to_html(text):
    """Convert markdown text to HTML."""
    logger.info("Converting markdown to HTML")
    return markdown.markdown(text, extensions=['tables', 'fenced_code'])

def html_to_flowables(html_content):
    """Convert HTML to ReportLab flowables."""
    logger.info("Parsing HTML to flowables")
    soup = BeautifulSoup(html_content, 'html.parser')
    flowables = []

    for element in soup:
        if element.name == 'h1':
            flowables.append(KeepTogether(Paragraph(element.text.strip(), styles['Title'])))
            flowables.append(Spacer(1, 0.25 * inch))
        elif element.name == 'h2':
            flowables.append(KeepTogether(Paragraph(element.text.strip(), styles['Heading1'])))
            flowables.append(Spacer(1, 0.2 * inch))
        elif element.name == 'h3':
            flowables.append(Paragraph(element.text.strip(), styles['Heading2']))
            flowables.append(Spacer(1, 0.15 * inch))
        elif element.name == 'p':
            text = element.text.strip()
            if text:
                flowables.append(Paragraph(text, styles['BodyText']))
                flowables.append(Spacer(1, 0.1 * inch))
        elif element.name == 'ul':
            for li in element.find_all('li'):
                text = li.text.strip()
                if text:
                    flowables.append(Paragraph(f"• {text}", styles['Bullet']))
                    flowables.append(Spacer(1, 0.05 * inch))
        elif element.name == 'ol':
            for i, li in enumerate(element.find_all('li'), 1):
                text = li.text.strip()
                if text:
                    flowables.append(Paragraph(f"{i}. {text}", styles['Bullet']))
                    flowables.append(Spacer(1, 0.05 * inch))
        elif element.name == 'img':
            src = element.get('src')
            if src and os.path.exists(src):
                try:
                    img = Image(src, width=4 * inch, height=2.5 * inch)
                    flowables.append(KeepTogether(img))
                    flowables.append(Spacer(1, 0.2 * inch))
                except Exception as e:
                    flowables.append(Paragraph(f"[Image failed to load: {str(e)}]", styles['BodyText']))
            else:
                flowables.append(Paragraph(f"[Image placeholder: {src}]", styles['BodyText']))
                flowables.append(Spacer(1, 0.1 * inch))
        elif element.name == 'table':
            data = []
            for tr in element.find_all('tr'):
                row = []
                for td in tr.find_all(['td', 'th']):
                    text = td.text.strip()
                    para = Paragraph(text, styles['TableText'])
                    row.append(para)
                data.append(row)
            if data:
                total_width = 504
                col_count = len(data[0])
                col_width = total_width / col_count
                col_widths = [col_width] * col_count
                table = Table(data, colWidths=col_widths, rowHeights=None)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 10),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 10),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                    ('BOX', (0, 0), (-1, -1), 0.5, colors.grey),
                    ('LEFTPADDING', (0, 0), (-1, -1), 12),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 12),
                    ('TOPPADDING', (0, 0), (-1, -1), 10),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
                ]))
                flowables.append(KeepTogether(table))
                flowables.append(Spacer(1, 0.2 * inch))
        elif element.name == 'hr':
            flowables.append(Spacer(1, 0.3 * inch))

    return flowables

def generate_pdf(content: str, output_path: str) -> str:
    """Generate a formatted PDF using ReportLab with two-pass page numbering."""
    logger.info(f"Starting PDF generation for {output_path}")
    doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=0.75 * inch, leftMargin=0.75 * inch, topMargin=0.75 * inch, bottomMargin=0.75 * inch)
    flowables = []


    html_content = markdown_to_html(content)
    flowables.extend(html_to_flowables(html_content))


    logger.info("Running first pass to count pages")
    temp_flowables = flowables[:]
    page_count = [0]

    def count_pages(canvas, doc):
        page_count[0] += 1

    doc.build(temp_flowables, onFirstPage=count_pages, onLaterPages=count_pages)


    logger.info(f"Running second pass with {page_count[0]} pages")
    doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=0.75 * inch, leftMargin=0.75 * inch, topMargin=0.75 * inch, bottomMargin=0.75 * inch)
    flowables = html_to_flowables(html_content)

    def add_page_number(canvas, doc):
        page_num = canvas.getPageNumber()
        canvas.saveState()
        canvas.setFont("Helvetica", 9)
        canvas.setFillColor(colors.grey)
        canvas.drawRightString(doc.pagesize[0] - 0.5 * inch, 0.5 * inch, f"Page {page_num} of {page_count[0]}")
        canvas.restoreState()

    doc.build(flowables, onFirstPage=add_page_number, onLaterPages=add_page_number)
    logger.info(f"PDF generated at {output_path}")
    return output_path