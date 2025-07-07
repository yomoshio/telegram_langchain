import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import markdown
from bs4 import BeautifulSoup
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define font paths relative to the script's location

FONT_DIR = Path("bot/fonts")
DEJAVU_SANS_PATH = os.path.join(FONT_DIR, 'DejaVuSans.ttf')
DEJAVU_SANS_BOLD_PATH = os.path.join(FONT_DIR, 'DejaVuSans-Bold.ttf')

# Register fonts with proper Cyrillic support
try:
    if os.path.exists(DEJAVU_SANS_PATH):
        pdfmetrics.registerFont(TTFont('DejaVuSans', DEJAVU_SANS_PATH))
        logger.info(f"Font DejaVuSans registered from {DEJAVU_SANS_PATH}")
    else:
        raise FileNotFoundError(f"Font file {DEJAVU_SANS_PATH} not found")

    if os.path.exists(DEJAVU_SANS_BOLD_PATH):
        pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', DEJAVU_SANS_BOLD_PATH))
        logger.info(f"Font DejaVuSans-Bold registered from {DEJAVU_SANS_BOLD_PATH}")
    else:
        logger.warning(f"Bold font file {DEJAVU_SANS_BOLD_PATH} not found, using DejaVuSans")
        pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', DEJAVU_SANS_PATH))
    font_name = 'DejaVuSans'
    bold_font_name = 'DejaVuSans-Bold'
except Exception as e:
    logger.error(f"Error registering fonts: {str(e)}, falling back to Helvetica (no Cyrillic support)")
    font_name = 'Helvetica'
    bold_font_name = 'Helvetica-Bold'

# Set up styles
styles = getSampleStyleSheet()
logger.info(f"Using fonts: regular={font_name}, bold={bold_font_name}")

for style_name in ['Title', 'Heading1', 'Heading2', 'BodyText', 'Bullet', 'TableText']:
    if style_name in styles:
        style = styles[style_name]
        style.fontName = bold_font_name if style_name in ['Title', 'Heading1', 'Heading2'] else font_name
        style.fontSize = {'Title': 20, 'Heading1': 16, 'Heading2': 14, 'BodyText': 11, 'Bullet': 11, 'TableText': 10}.get(style_name, 10)
        style.leading = {'Title': 24, 'Heading1': 20, 'Heading2': 18, 'BodyText': 14, 'Bullet': 14, 'TableText': 12}.get(style_name, 12)
        style.spaceAfter = {'Title': 16, 'Heading1': 12, 'Heading2': 10, 'BodyText': 10, 'Bullet': 6, 'TableText': 0}.get(style_name, 0)
        style.textColor = {'Title': colors.navy, 'Heading1': colors.darkblue, 'Heading2': colors.darkblue,
                          'BodyText': colors.black, 'Bullet': colors.black, 'TableText': colors.black}.get(style_name, colors.black)
        style.alignment = {'Title': 1, 'Heading1': 0, 'Heading2': 0}.get(style_name, 0)  # Center Title, left-align others
        if style_name == 'Bullet':
            style.leftIndent = 30
            style.bulletIndent = 15
        if style_name == 'Heading1':
            style.backColor = colors.HexColor('#F0F0F0')  # Light grey background
        logger.info(f"Updated style {style_name} with fontName={style.fontName}")
    else:
        if style_name == 'TableText':
            styles.add(ParagraphStyle(name='TableText', fontName=font_name, fontSize=10, leading=12, textColor=colors.black))
            logger.info(f"Created new style TableText with fontName={font_name}")

def markdown_to_html(text):
    """Convert markdown text to HTML."""
    logger.info("Converting markdown to HTML")
    html = markdown.markdown(text, extensions=['tables', 'fenced_code'])
    return html.replace('\n', '<br/>')  # Ensure line breaks are preserved

def html_to_flowables(html_content):
    """Convert HTML to ReportLab flowables."""
    logger.info("Parsing HTML to flowables")
    soup = BeautifulSoup(html_content, 'html.parser')
    flowables = []

    for element in soup:
        if element.name == 'h1':
            flowables.append(KeepTogether(Paragraph(element.text.strip(), styles['Title'])))
            flowables.append(Spacer(1, 0.3 * inch))
        elif element.name == 'h2':
            flowables.append(KeepTogether(Paragraph(element.text.strip(), styles['Heading1'])))
            flowables.append(Spacer(1, 0.2 * inch))
        elif element.name == 'h3':
            flowables.append(Paragraph(element.text.strip(), styles['Heading2']))
            flowables.append(Spacer(1, 0.15 * inch))
        elif element.name == 'p':
            text = element.decode_contents().strip()  # Preserve <br/> for line breaks
            if text:
                flowables.append(Paragraph(text, styles['BodyText']))
                flowables.append(Spacer(1, 0.1 * inch))
        elif element.name == 'ul':
            for li in element.find_all('li'):
                text = li.decode_contents().strip()
                if text:
                    flowables.append(Paragraph(f"• {text}", styles['Bullet']))
                    flowables.append(Spacer(1, 0.05 * inch))
        elif element.name == 'ol':
            for i, li in enumerate(element.find_all('li'), 1):
                text = li.decode_contents().strip()
                if text:
                    flowables.append(Paragraph(f"{i}. {text}", styles['Bullet']))
                    flowables.append(Spacer(1, 0.05 * inch))
        elif element.name == 'table':
            data = []
            for tr in element.find_all('tr'):
                row = [Paragraph(td.decode_contents().strip(), styles['TableText']) for td in tr.find_all(['td', 'th'])]
                data.append(row)
            if data:
                total_width = 7 * inch  # Adjusted for letter page with margins
                col_count = len(data[0])
                col_width = total_width / max(col_count, 1)
                table = Table(data, colWidths=[col_width] * col_count)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E6F0FA')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                    ('FONTNAME', (0, 0), (-1, 0), bold_font_name),
                    ('FONTSIZE', (0, 0), (-1, 0), 10),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                    ('FONTNAME', (0, 1), (-1, -1), font_name),
                    ('FONTSIZE', (0, 1), (-1, -1), 10),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                    ('BOX', (0, 0), (-1, -1), 0.5, colors.grey),
                    ('LEFTPADDING', (0, 0), (-1, -1), 6),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                    ('TOPPADDING', (0, 0), (-1, -1), 6),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F8F8')]),
                ]))
                flowables.append(KeepTogether(table))
                flowables.append(Spacer(1, 0.2 * inch))
        elif element.name == 'hr':
            flowables.append(Spacer(1, 0.3 * inch))

    return flowables

def generate_pdf(content: str, output_path: str) -> str:
    """Generate a formatted PDF using ReportLab with two-pass page numbering."""
    logger.info(f"Starting PDF generation for {output_path}")
    doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=0.75 * inch, leftMargin=0.75 * inch,
                            topMargin=0.75 * inch, bottomMargin=0.75 * inch)

    try:
        pdfmetrics.registerFont(TTFont(font_name, DEJAVU_SANS_PATH))
        if bold_font_name != font_name:
            pdfmetrics.registerFont(TTFont(bold_font_name, DEJAVU_SANS_BOLD_PATH if os.path.exists(DEJAVU_SANS_BOLD_PATH) else DEJAVU_SANS_PATH))
        
        html_content = markdown_to_html(content)
        flowables = html_to_flowables(html_content)

        # First pass to count pages
        logger.info("Running first pass to count pages")
        page_count = [0]
        def count_pages(canvas, doc):
            page_count[0] += 1
        doc.build(flowables, onFirstPage=count_pages, onLaterPages=count_pages)

        # Second pass to generate PDF with page numbers
        logger.info(f"Running second pass with {page_count[0]} pages")
        doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=0.75 * inch, leftMargin=0.75 * inch,
                                topMargin=0.75 * inch, bottomMargin=0.75 * inch)
        pdfmetrics.registerFont(TTFont(font_name, DEJAVU_SANS_PATH))
        if bold_font_name != font_name:
            pdfmetrics.registerFont(TTFont(bold_font_name, DEJAVU_SANS_BOLD_PATH if os.path.exists(DEJAVU_SANS_BOLD_PATH) else DEJAVU_SANS_PATH))
        flowables = html_to_flowables(html_content)

        def add_page_number(canvas, doc):
            page_num = canvas.getPageNumber()
            canvas.saveState()
            canvas.setFont(font_name, 9)
            canvas.setFillColor(colors.grey)
            canvas.drawCentredString(doc.pagesize[0] / 2, 0.5 * inch, f"Страница {page_num} из {page_count[0]}")
            canvas.restoreState()

        doc.build(flowables, onFirstPage=add_page_number, onLaterPages=add_page_number)
        logger.info(f"PDF generated at {output_path}")
        return output_path
    except Exception as e:
        logger.error(f"Error in PDF generation: {str(e)}")
        raise