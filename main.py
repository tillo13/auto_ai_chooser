from flask import Flask, render_template, request, redirect, url_for
#import code from existing .py code in the app:
from chatgpt_utils import get_response_for_user_input
#from secrets_manager import get_secret_version
from config import SITE_HOMEPAGE,GCP_PROJECT_ID, OPENAI_SECRET_KEY, OPENAI_DEFAULT_MODEL
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('input_box')  # get the value from 'input_box'
        return redirect(url_for('result', input=user_input))  # pass the value to 'result'
    return render_template('index.html')

@app.route('/result')
def result():
    user_input = request.args.get('input', 'empty')
    if user_input != 'empty':
        try:
            from chatgpt_utils import get_chatgpt_response
            full_gpt_response, chatgpt_time = get_chatgpt_response(user_input, OPENAI_DEFAULT_MODEL, OPENAI_SECRET_KEY)
            user_input += f"ChatGPT Response: {json.dumps(full_gpt_response, indent=2)}"
        except Exception as e:
            print(f"Failed to get chatGPT response. Error: {e}")
            chatgpt_time = 0
    return f"You typed: {user_input}"

if __name__ == "__main__":
    app.run(debug=True)