#!/usr/bin/env python3
"""
Flask: module to run a flask app
render_template: used to render an html page
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    Simple route that leads to index.html
    template.
    """
    return render_template('0-index.html')
