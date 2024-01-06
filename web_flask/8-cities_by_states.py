#!/usr/bin/python3
""" starts a Flask web application with specified requirements
"""

from flask import Flask, render_template
import models
from models.state import State, storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def state_display():
    """ display a HTML page with list of state object """
    states = models.storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    """execute when run directly"""
    app.run(host="0.0.0.0", port=5000)
