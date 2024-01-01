#!/usr/bin/python3
"""starts a flask web application"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """displays hbnb"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns hbnb"""

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def val(text):
    """display C followed by the value of the text"""

    formatted_text = text.replace('_', ' ')
    return f"C {escape(formatted_text)}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
def py_thon(text):
    """dispaly text with default provided"""

    formatted_text = text.replace('_', ' ')
    return f"Python {escape(formatted_text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """return n if its a number"""

    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an interger"""

    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """display whether its even or odd"""

    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    """execute when run directly"""

    app.run(host="0.0.0.0", port=5000)
