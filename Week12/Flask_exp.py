from flask import Flask


app = Flask(__name__)


@app.route('/admin')
def hello_world():
    return 'Hello Flask!'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
