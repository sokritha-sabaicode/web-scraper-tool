from constants.models_costs import (
    MODEL_COST_PER_1K_TOKENS_INPUT, 
    MODEL_COST_PER_1K_TOKENS_OUTPUT
)

def calculate_token_cost(model_name, prompt_tokens, completion_tokens):
    """
    Given a model name and token usage, returns the total estimated cost.
    """
    input_cost = MODEL_COST_PER_1K_TOKENS_INPUT.get(model_name, 0)
    output_cost = MODEL_COST_PER_1K_TOKENS_OUTPUT.get(model_name, 0)
    total_cost = (prompt_tokens / 1000) * input_cost + (completion_tokens / 1000) * output_cost
    return total_cost
