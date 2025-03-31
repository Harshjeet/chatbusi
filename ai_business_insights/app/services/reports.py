from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
import os

def format_response_for_report(response):
    sections = response.split("\n\n")

    report_content = {
        "Summary": sections[0] if len(sections) > 0 else "No summary available.",
        "Detailed Insights": sections[1] if len(sections) > 1 else "No detailed insights.",
        "Recommendations": sections[2] if len(sections) > 2 else "No recommendations."
    }

    return report_content

def generate_pdf_report(response, output_path="report.pdf"):
   
    report_content = format_response_for_report(response)

    
    doc = SimpleDocTemplate(output_path, pagesize=LETTER)
    styles = getSampleStyleSheet()
    content = []

   
    content.append(Paragraph("Business Insights Report", styles['Title']))
    content.append(Spacer(1, 12))

    
    for section, text in report_content.items():
        content.append(Paragraph(f"<b>{section}</b>", styles['Heading2']))
        content.append(Spacer(1, 6))
        content.append(Paragraph(text, styles['BodyText']))
        content.append(Spacer(1, 12))

    doc.build(content)
    return output_path

def generate_csv_report(response, output_path="report.csv"):
    """
    Generate a CSV report from the AI-generated insights.
    """
    report_content = format_response_for_report(response)

    # Create DataFrame
    df = pd.DataFrame(list(report_content.items()), columns=["Section", "Content"])

    # Save as CSV
    df.to_csv(output_path, index=False)
    return output_path
