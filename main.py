from flask import Flask, render_template, request, redirect, url_for
#import code from existing .py code in the app:
from chatgpt_utils import get_response_for_user_input, get_chatgpt_response
#from secrets_manager import get_secret_version
from config import SITE_HOMEPAGE,GCP_PROJECT_ID, OPENAI_SECRET_KEY, OPENAI_DEFAULT_MODEL
import json
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)  # Configure the logging level

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('input_box')  # get the value from 'input_box'
        model_choice = request.form.get('model')  # get the selected model
        return redirect(url_for('result', input=user_input, model=model_choice))  # pass the value to 'result'
    return render_template('index.html')

@app.route('/result')
def result():
    user_input = request.args.get('input', 'empty')
    model_choice = request.args.get('model', 'gpt-4')  # get the model from the URL, default to 'gpt-4'
    if user_input != 'empty':
        try:
            full_gpt_response = get_response_for_user_input(user_input, model_choice, OPENAI_SECRET_KEY)
            user_input += f"\nChatGPT Full Response: {full_gpt_response}"
        except Exception as e:
            print(f"Failed to get chatGPT response. Error: {e}")
    return f"You typed: {user_input}"

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/result')
def result():
    # Load the openai prices json
    with open("openai_pricing.json") as f:
        prices = json.load(f)
    user_input = request.args.get('input', 'empty')
    model_choice = request.args.get('model', OPENAI_DEFAULT_MODEL)  # get the model from the URL, default to OPENAI_DEFAULT_MODEL
    if user_input != 'empty':
        try:
            from chatgpt_utils import get_chatgpt_response
            full_gpt_response, max_tokens, chatgpt_time = get_chatgpt_response(user_input, model_choice, OPENAI_SECRET_KEY)
            # You can adjust below depending on your model_choice and it's context size (if you allow the users to select models with different context sizes)
            cost_per_token = prices[model_choice]["8k"]["output"]
            total_cost = (max_tokens/1000) * cost_per_token
            user_input += f"\nChatGPT Response: {json.dumps(full_gpt_response, indent=2)}"
            user_input += f"\nMax Tokens used: {max_tokens}"
            user_input += f"\nTotal estimated cost: ${total_cost:.2f}"
        except Exception as e:
            app.logger.exception("Failed to get chatGPT response.")  # Use logging.exception inside the except block
            print(f"Failed to get chatGPT response. Error: {e}")
            chatgpt_time = 0
    return f"You typed: {user_input}"

if __name__ == "__main__":
    app.run(debug=True)