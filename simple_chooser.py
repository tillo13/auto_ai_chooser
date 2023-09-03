import json
import os
from langchain.llms import OpenAI as LangChainOpenAI
import openai
from dotenv import load_dotenv

# Load the .env file to read the api key
load_dotenv()

# Use the api key from the env file
api_key = os.getenv("OPENAI_API_KEY")

# Load pricing details
with open("openai_pricing.json") as f:
    pricing = json.load(f)

def direct_openai_api(api_key, user_input):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    # Print the full response JSON
    print("Full response from OpenAI API:")
    print(json.dumps(response, indent=2, sort_keys=True))

    total_tokens = response["usage"]["total_tokens"]
    estimated_cost = pricing["gpt-3.5"]["16k"]["output"] * total_tokens

    return response["choices"][0]["message"]["content"], estimated_cost

def langchain_openai_api(api_key, user_input):
    llm = LangChainOpenAI(openai_api_key=api_key)
    result = llm.predict(user_input)

    # Since we do not have the full response payload for LangChain's predict method
    # Printing just the result
    print("Full response from LangChain API:")
    print(result)

    # Obtain price estimation
    # As I don't have the detail of how LangChain calculates the tokens, assuming it same as OpenAI's gpt-3.5 model
    total_tokens = len(user_input.split())
    estimated_cost = pricing["gpt-3.5"]["16k"]["output"] * total_tokens

    return result, estimated_cost

def main():
    user_input = input("Enter your message to the AI: ")

    print("\n1. Direct OpenAI")
    print("2. LangChain OpenAI")
    choice = int(input("\nChoose your AI service: "))

    if choice == 1:
        result, cost = direct_openai_api(api_key, user_input)
    elif choice == 2:
        result, cost = langchain_openai_api(api_key, user_input)
    else:
        print("Invalid choice")
        return

    print("\nAI's Response: ", result)
    print("Estimated cost: ", cost)

if __name__ == "__main__":
    main()