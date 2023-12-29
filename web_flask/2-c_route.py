#!/usr/bin/python3
"""starts a flask web application"""

from flask import Flask
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


if __name__ == "__main__":
    """execute when run directly"""

    app.run(host="0.0.0.0", port=5000)
