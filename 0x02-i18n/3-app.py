#!/usr/bin/env python3
"""
Flask: module to run our flask app
render_template: renders an html page
Bable: used to create an instance of bable
gettext: used for translating the header and the title
"""
from flask import Flask, render_template
from flask_babel import Babel, gettext as _


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """
    index function is used to direct the route towards the translations
    """
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world!")

    return render_template(
            '3-index.html',
            title=home_title,
            header=home_header)
