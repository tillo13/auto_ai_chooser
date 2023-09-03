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
    model_choice = request.args.get('model', OPENAI_DEFAULT_MODEL)  # get the model from the URL, default to OPENAI_DEFAULT_MODEL
    if user_input != 'empty':
        try:
            full_gpt_response, max_tokens, chatgpt_time = get_chatgpt_response(user_input, model_choice, OPENAI_SECRET_KEY)
            user_input += f"\nChatGPT Response: {full_gpt_response}"
            user_input += f"\nTotal tokens used: {max_tokens}"
        except Exception as e:
            app.logger.exception("Failed to get chatGPT response.")  # Use logging.exception inside the except block
            print(f"Failed to get chatGPT response. Error: {e}")
            chatgpt_time = 0
    return f"You typed: {user_input}"

if __name__ == "__main__":
    app.run(debug=True)