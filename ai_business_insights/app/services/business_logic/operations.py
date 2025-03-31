from app.services.gemini_service import generate_gemini_response

def handle_operations_query(query, entities):
    """
    Handle operations-specific queries by creating tailored prompts.
    """
    # Operations-specific prompt
    prompt = f"""
    You are an operations expert.
    Query: {query}

    Provide:
    - Operational efficiency insights.
    - Process optimization strategies.
    - Workflow improvement recommendations.

    Extracted entities: {entities}
    """

    # Generate the response
    response = generate_gemini_response(prompt)
    return response
