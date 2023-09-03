import openai
import time
from openai import OpenAIError
from tiktoken import Tokenizer, models

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

    try:
        response = openai.ChatCompletion.create(
            model=model_choice,
            messages=messages,
            temperature=0.6,
            max_tokens=500
        )
        
        # Count tokens using tiktoken
        tokenizer = Tokenizer(models.Model())
        user_input_tokens = len(list(tokenizer.encode(user_input)))
        gpt_response_tokens = len(list(tokenizer.encode(response['choices'][0]['message']['content'])))
        total_tokens = user_input_tokens + gpt_response_tokens

        return response, total_tokens
    except OpenAIError as e:
        print(e)
        return str(e), 0