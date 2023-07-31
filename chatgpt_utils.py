import os
import time
import openai
import tiktoken

def get_chatgpt_response(user_input, model_choice, openai_secret_key):
    start_time = time.time()
    full_response, max_tokens = get_response_for_user_input(user_input, model_choice, openai_secret_key)
    duration = time.time() - start_time
    return full_response, max_tokens, duration

def get_response_for_user_input(user_input, model_choice, openai_secret_key):
    openai.api_key = openai_secret_key

    messages=[
        {"role": "system", "content":"You are a helpful assistant."},
        {"role": "user", "content": user_input},
    ]

    response = openai.ChatCompletion.create(
        model=model_choice,
        messages=messages,
        temperature=0.6,
        max_tokens=500
    )

    return response