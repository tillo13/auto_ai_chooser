from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('input_box')  # get the value from 'input_box'
        return redirect(url_for('result', input=user_input))  # pass the value to 'result'
    return render_template('index.html')

@app.route('/result')
def result():
    user_input = request.args.get('input', 'empty')  # get the value from 'input_box' or default 'empty'
    return f"You typed: {user_input}"

if __name__ == "__main__":
    app.run(debug=True)