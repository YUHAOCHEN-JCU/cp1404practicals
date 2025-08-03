from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    if name:
        return f"<h2>Hello {name}!</h2>"
    else:
        return "<h2>Hello!</h2>"


app.run(host='127.0.0.8', port=8080, debug=True)

