#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb():
    """fuction defination"""

    return "Hello HBNB!"


if __name__ == "__main__":
    """Execute when run directly"""

    app.run(host="0.0.0.0", port=5000)
