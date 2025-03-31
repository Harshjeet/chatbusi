from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
import re
from xhtml2pdf import pisa
from markdown2 import markdown
import os

def generate_pdf_report(response, output_path="report.pdf"):
    """
    Generate a PDF report with properly formatted markdown content.
    """
    # Convert Markdown to HTML
    html_content = markdown(response)

    # Add basic styling for better formatting
    html_template = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
            }}
            h1, h2, h3 {{
                color: #333;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            table, th, td {{
                border: 1px solid #ccc;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            p {{
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        <h1>Business Insights Report</h1>
        {html_content}
    </body>
    </html>
    """

    # Generate PDF
    with open(output_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_template, dest=pdf_file)

    if not pisa_status.err:
        return output_path
    else:
        raise Exception("Failed to generate PDF.")
def extract_table_from_response(response):
    """
    Extracts a table from the AI-generated response using regex.
    """
    table_pattern = r'\|(.+?)\|\n(\|[-:]+\|)+\n((?:\|.*?\|\n?)+)'
    match = re.search(table_pattern, response, re.DOTALL)

    if match:
        headers = [h.strip() for h in match.group(1).split('|') if h.strip()]
        rows = [row.split('|')[1:-1] for row in match.group(3).split('\n') if row.strip()]

        df = pd.DataFrame(rows, columns=headers)
        return df
    return None


def generate_csv_report(response, output_path="report.csv"):
    """
    Generate a CSV report if table is found in the response.
    """
    df = extract_table_from_response(response)

    if df is not None:
        df.to_csv(output_path, index=False)
        return output_path
    else:
        return None
