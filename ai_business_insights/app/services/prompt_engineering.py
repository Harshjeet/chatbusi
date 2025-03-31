from langchain.prompts import PromptTemplate

def generate_single_prompt(query, entities):
    """
    Generate a single-step prompt for basic business queries.
    """
    template = """
    You are a business insights assistant. 
    Analyze the following business query and provide a structured and detailed response.

    Query: {query}

    Entities Identified: {entities}

    Provide insights including:
    - Key points and findings
    - Recommendations
    - Potential business impacts
    """

    prompt = PromptTemplate(
        input_variables=["query", "entities"],
        template=template
    )

    return prompt.format(query=query, entities=entities)

def generate_multi_step_prompts(query, entities):
    """
    Generate multi-step prompts for complex business queries.
    """
    step_1 = f"""
    Step 1: Identify the key components of the query.
    Query: {query}
    Entities: {entities}
    
    Provide a breakdown of the query into individual objectives.
    """

    step_2 = f"""
    Step 2: Generate insights for each objective identified in Step 1.
    Provide structured analysis for each component.
    """

    step_3 = f"""
    Step 3: Consolidate the insights from Step 2 into a comprehensive business recommendation.
    Include:
    - Key findings
    - Suggested strategies
    - Potential business impacts
    """

    return [step_1, step_2, step_3]
