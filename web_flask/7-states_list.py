#!/usr/bin/python3
""" starts a Flask web application with specified requirements
"""

import sys
from flask import Flask, render_template
from models import storage
from models.state import State
sys.path.append("..")

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_display():
    """ display a HTML page with list of state object """
    statess = storage.all(State).values()

    return render_template("7-states_list.html", states=statess)


if __name__ == "__main__":
    """execute when run directly"""
    app.run(host="0.0.0.0", port=5000)
