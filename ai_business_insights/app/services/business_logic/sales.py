from app.services.gemini_service import generate_gemini_response

def handle_sales_query(query, entities):
    """
    Handle sales-specific queries by creating tailored prompts.
    """
    # Sales-specific prompt
    prompt = f"""
    You are a sales consultant.
    Query: {query}

    Provide:
    - Sales performance insights.
    - Lead generation strategies.
    - Revenue optimization recommendations.

    Extracted entities: {entities}
    """

    # Generate the response
    response = generate_gemini_response(prompt)
    return response
