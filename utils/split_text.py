import tiktoken


def chunk_text_by_tokens(text, max_tokens=3000, model_name="gpt-3.5-turbo"):
    """
    Splits a given text into chunks of ~max_tokens using tiktoken
    so we don't exceed the model's context limit.
    """
    # Get encoding for your chosen model
    encoding = tiktoken.encoding_for_model(model_name)

    # Encode the entire text to tokens
    tokens = encoding.encode(text)

    # Yield slices of tokens
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i : i + max_tokens]
        # Decode tokens back to text
        yield encoding.decode(chunk_tokens)