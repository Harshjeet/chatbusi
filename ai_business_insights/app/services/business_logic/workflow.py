from concurrent.futures import ThreadPoolExecutor, as_completed
from app.services.business_logic.finance import handle_finance_query
from app.services.business_logic.marketing import handle_marketing_query
from app.services.business_logic.sales import handle_sales_query
from app.services.business_logic.operations import handle_operations_query

def execute_workflow(query, entities):
    """
    Execute a multi-step workflow based on the query and detected business functions.

    Returns:
    - Combined results from different business function handlers.
    """
    # Identify relevant business functions
    functions = []
    
    # Detect relevant functions based on query keywords
    if "finance" in query.lower():
        functions.append("finance")
    if "marketing" in query.lower():
        functions.append("marketing")
    if "sales" in query.lower():
        functions.append("sales")
    if "operations" in query.lower():
        functions.append("operations")

    if not functions:
        functions.append("general")  # Fallback for general responses

    results = {}

    # Parallel execution using ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        future_to_function = {
            executor.submit(
                execute_function, func, query, entities
            ): func for func in functions
        }

        for future in as_completed(future_to_function):
            func_name = future_to_function[future]
            try:
                result = future.result()
                results[func_name] = result
            except Exception as e:
                results[func_name] = f"Error: {str(e)}"

    return results

def execute_function(func, query, entities):
    """
    Execute the appropriate handler based on the business function.
    """
    if func == "finance":
        return handle_finance_query(query, entities)
    elif func == "marketing":
        return handle_marketing_query(query, entities)
    elif func == "sales":
        return handle_sales_query(query, entities)
    elif func == "operations":
        return handle_operations_query(query, entities)
    else:
        return "General business insights unavailable."
