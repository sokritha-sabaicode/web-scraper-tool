"""
Cost for 1k tokens in input
"""

MODEL_COST_PER_1K_TOKENS_INPUT = {
    ### OPENAI
    "gpt-4o": 0.0025,
    "gpt-4o-mini": 0.000150,
    "gpt-3.5-turbo": 0.0005,
}

"""
Cost for 1k tokens in output
"""
MODEL_COST_PER_1K_TOKENS_OUTPUT = {
    # General Purpose
    "gpt-4o": 0.01,
    "gpt-4o-mini": 0.0006,
    "gpt-3.5-turbo": 0.00150,
}


"""
https://openai.com/api/pricing/
"""
