import json

def test_query_route(client):
    """
    Test the main query route.
    """
    payload = {"query": "Analyze Apple's financial growth."}
    response = client.post('/api/query', json=payload)

    assert response.status_code == 200
    data = response.get_json()
    
    assert "original_query" in data
    assert "business_function" in data
    assert "response" in data

def test_query_route_no_query(client):
    """
    Test query route without query.
    """
    response = client.post('/api/query', json={})
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_query_route_invalid_json(client):
    """
    Test query route with invalid JSON.
    """
    response = client.post('/api/query', data="Invalid")
    assert response.status_code == 400
    assert "error" in response.get_json()
