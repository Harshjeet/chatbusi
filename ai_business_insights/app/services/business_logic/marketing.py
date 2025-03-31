from app.services.gemini_service import generate_gemini_response

def handle_marketing_query(query, entities):
    """
    Handle marketing-specific queries by creating tailored prompts.
    """
    # Marketing-specific prompt
    prompt = f"""
    You are a marketing strategist.
    Query: {query}

    Provide:
    - Current market trends.
    - Competitor analysis.
    - Suggested marketing strategies.

    Extracted entities: {entities}
    """

    # Generate the response
    response = generate_gemini_response(prompt)
    return response
