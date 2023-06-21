from flask import Flask, render_template, request
import gpt4all

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'secret_key'

PATH = '/Users/ymg/Library/Application Support/nomic.ai/GPT4All/GPT4All-13B-snoozy.ggmlv3.q4_0.bin'
mpt = gpt4all.GPT4All(PATH, model_type='mpt')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    message = [{"role": "user", "content": user_input}]
    response = mpt.chat_completion(message)
    content = response['choices'][0]['message']['content']
    return content

if __name__ == '__main__':
    app.run(debug=True)
