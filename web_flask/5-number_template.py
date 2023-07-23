#!/usr/bin/python3
"""
This module contains a code that starts a Flask web application
"""
from flask import Flask, abort, render_template
import re
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a string """
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string """
    return f'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns a string """
    return 'C ' + text.replace('_', ' ')


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_str(text="is cool"):
    """Returns a string """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """Returns a formated string"""
    pattern = r"^[0-9]+$"
    if re.match(pattern, n):
        return f'{n} is a number'
    else:
        """We can also user abort function to return a custom error message.
        ex: abort(404,'The requested URL does not exist'"""
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """Display HTML page only if n is an integer """
    pattern = r"^[0-9]+$"
    if re.match(pattern, n):
        return render_template('5-number.html', number=n)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)
