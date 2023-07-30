import os
import time
import openai

def get_chatgpt_response(user_input, model_choice, openai_secret_key):
    start_time = time.time()
    response = get_response_for_user_input(user_input, model_choice, openai_secret_key)
    duration = time.time() - start_time
    return response, duration

def get_response_for_user_input(user_input, incoming_model, openai_secret_key):
    openai.api_key = openai_secret_key

    prompt = f"{user_input}"

    if incoming_model == "gpt-3.5-turbo":
        messages=[
            {"role": "system", "content":"You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]

        response = openai.ChatCompletion.create(
        model=incoming_model,
        messages=messages,
        temperature=0.6,
        max_tokens=1000
        )
        result = response.choices[0].message['content'].strip()

    elif incoming_model == "text-davinci-003":
        response = openai.Completion.create(engine=incoming_model, prompt=prompt, max_tokens=1000)
        result = response.choices[0].text.strip()

    else:
        result = "Model not recognized.  Contact your local developer."

    return result
