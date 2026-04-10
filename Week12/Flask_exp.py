from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/admin')
def hello_world():
    return 'Hello Flask Framework!'

@app.route('/bye')
def bye_world():
    return 'Bye Flask Framework!'

if __name__ == '__main__':
    app.run(debug=True)