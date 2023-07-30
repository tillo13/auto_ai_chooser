import os
import time
import tiktoken
import openai

def get_chatgpt_response(user_input, model_choice, openai_secret_key):
    start_time = time.time()
    full_response = get_response_for_user_input(user_input, model_choice, openai_secret_key)
    duration = time.time() - start_time
    return full_response, duration

def get_response_for_user_input(user_input, incoming_model, openai_secret_key):
    openai.api_key = openai_secret_key

    prompt = f"{user_input}"

    tokenizer = tiktoken.get_encoding("cl100k_base")  # Use default encoding
    input_tokens = len(tokenizer.encode(prompt))

    # Define a buffer for the message structure (might need adjustment)
    message_buffer = 50

    # Define a maximum value for response tokens (might need adjustment)
    max_response_tokens = 500

    if incoming_model.startswith("gpt-3.5"):
        if incoming_model.endswith("16k"):
            model_max_tokens = 16384  # GPT-3.5 Turbo 16K
        else:
            model_max_tokens = 4096   # other GPT-3.5 models

    elif incoming_model.startswith("text-davinci"):
        model_max_tokens = 4097   # Text Davinci models

    elif incoming_model.startswith("code-davinci"):
        model_max_tokens = 8001   # Code Davinci models

    elif incoming_model.startswith("gpt-4"):
        if incoming_model.endswith("32k"):
            model_max_tokens = 32768  # GPT-4 32K models
        else:
            model_max_tokens = 8192   # other GPT-4 models

    else:
        return "Model not recognized.  Contact your local developer."

    messages=[
        {"role": "system", "content":"You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]

    max_tokens = min(model_max_tokens - input_tokens - message_buffer, max_response_tokens)

    response = openai.ChatCompletion.create(
        model=incoming_model,
        messages=messages,
        temperature=0.6,
        max_tokens=max_tokens
    )

    # Instead of returning a single message, return the entire response
    return response
