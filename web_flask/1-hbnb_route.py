#!/usr/bin/python3
"""
This module contains a code that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a string """
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string """
    return f'HBNB'


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)
