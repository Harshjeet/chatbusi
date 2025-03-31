from app.utils.preprocessor import clean_query, extract_entities, detect_query_type

def test_clean_query():
    """
    Test cleaning of queries.
    """
    query = "   Analyze the Market!   "
    cleaned = clean_query(query)
    assert cleaned == "analyze the market"

def test_extract_entities():
    """
    Test entity extraction.
    """
    query = "Show Tesla's revenue in 2023."
    entities = extract_entities(query)
    assert "Tesla" in entities
    assert "2023" in entities

def test_detect_query_type():
    """
    Test query type detection.
    """
    query1 = "What are the top marketing trends for 2025?"
    query2 = "Generate a step-by-step analysis of market trends."

    assert detect_query_type(query1) == "single-step"
    assert detect_query_type(query2) == "multi-step"
