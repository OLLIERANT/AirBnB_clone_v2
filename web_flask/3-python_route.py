#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """print web"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """print C followed by the value of the text variable"""
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


# Define the route for '/python/<text>
@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """print python followed by the value of the text variable"""
    formatted_text = text.replace('_', ' ')
    return "python {}".format(formatted_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
