from app.services.gemini_service import generate_gemini_response

def handle_finance_query(query, entities):
    """
    Handle finance-specific queries by creating tailored prompts.
    """
    # Finance-specific prompt
    prompt = f"""
    You are a financial business analyst. 
    Query: {query}

    Provide:
    - A financial summary.
    - Key metrics or trends.
    - Recommendations for financial improvements.

    Extracted entities: {entities}
    """

    # Generate the response
    response = generate_gemini_response(prompt)
    return response
