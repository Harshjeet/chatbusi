from flask import Blueprint, request, jsonify, send_file
from app.services.gemini_service import generate_gemini_response, generate_multi_step_response
from app.utils.preprocessor import clean_query, extract_entities, detect_query_type
from app.services.prompt_engineering import generate_single_prompt, generate_multi_step_prompts
from app.services.reports import generate_pdf_report, generate_csv_report, extract_table_from_response
from app.services.business_logic.workflow import execute_workflow

# Importing specific business function handlers
from app.services.business_logic.finance import handle_finance_query
from app.services.business_logic.marketing import handle_marketing_query
from app.services.business_logic.sales import handle_sales_query
from app.services.business_logic.operations import handle_operations_query

import os

# Create a Blueprint for query routes
query_bp = Blueprint('query_bp', __name__)

@query_bp.route('/query', methods=['POST'])
def handle_query():
    """
    Handle business queries with business function detection and multi-step execution.
    """
    try:
        data = request.get_json()
        query = data.get("query", "")

        if not query:
            return jsonify({"error": "No query provided"}), 400

        # Preprocessing
        cleaned_query = clean_query(query)
        entities = extract_entities(query)
        query_type = detect_query_type(query)

        # Business function detection
        business_function = None
        if "finance" in query.lower():
            business_function = "finance"
        elif "marketing" in query.lower():
            business_function = "marketing"
        elif "sales" in query.lower():
            business_function = "sales"
        elif "operations" in query.lower():
            business_function = "operations"

        # Execution logic
        if business_function:
            # Use specific handlers for known business functions
            if business_function == "finance":
                response = handle_finance_query(cleaned_query, entities)
            elif business_function == "marketing":
                response = handle_marketing_query(cleaned_query, entities)
            elif business_function == "sales":
                response = handle_sales_query(cleaned_query, entities)
            elif business_function == "operations":
                response = handle_operations_query(cleaned_query, entities)
            structured_response = {
                "original_query": query,
                "business_function": business_function,
                "response": response
            }

        else:
            # Fallback to Gemini for multi-step or general queries
            if query_type == "multi-step":
                prompts = generate_multi_step_prompts(cleaned_query, entities)
                response = generate_multi_step_response(prompts)
            else:
                prompt = generate_single_prompt(cleaned_query, entities)
                response = generate_gemini_response(prompt)

            structured_response = {
                "original_query": query,
                "business_function": "general",
                "response": response
            }

        return jsonify(structured_response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@query_bp.route('/download/pdf', methods=['POST'])
def download_pdf():
    """
    Download the AI insights as a properly formatted PDF report.
    """
    try:
        data = request.get_json()
        response = data.get("response", "")

        if not response:
            return jsonify({"error": "No response provided"}), 400

        output_path = "output/report.pdf"
        
        # Ensure the output directory exists
        if not os.path.exists("output"):
            os.makedirs("output")

        # Generate the formatted PDF
        generate_pdf_report(response, output_path)
        
        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@query_bp.route('/download/csv', methods=['POST'])
def download_csv():
    """
    Download AI insights table as a CSV report if table exists.
    """
    try:
        data = request.get_json()
        response = data.get("response", "")

        if not response:
            return jsonify({"error": "No response provided"}), 400

        table_df = extract_table_from_response(response)

        if table_df is None:
            return jsonify({"error": "No table found in response"}), 400

        output_path = "output/report.csv"
        if not os.path.exists("output"):
            os.makedirs("output")

        table_df.to_csv(output_path, index=False)
        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500