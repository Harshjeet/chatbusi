from app.services.business_logic.finance import handle_finance_query
from app.services.business_logic.marketing import handle_marketing_query
from app.services.business_logic.sales import handle_sales_query
from app.services.business_logic.operations import handle_operations_query

def test_finance_query():
    """
    Test finance business logic.
    """
    query = "Analyze Tesla's Q4 2024 revenue."
    response = handle_finance_query(query, ["Tesla", "2024"])
    assert "revenue" in response.lower()

def test_marketing_query():
    """
    Test marketing business logic.
    """
    query = "Identify top marketing strategies for e-commerce."
    response = handle_marketing_query(query, ["e-commerce"])
    assert "strategies" in response.lower()

def test_sales_query():
    """
    Test sales business logic.
    """
    query = "Suggest ways to boost Q3 sales."
    response = handle_sales_query(query, ["Q3"])
    assert "sales" in response.lower()

def test_operations_query():
    """
    Test operations business logic.
    """
    query = "Improve supply chain efficiency."
    response = handle_operations_query(query, ["supply chain"])
    assert "efficiency" in response.lower()
