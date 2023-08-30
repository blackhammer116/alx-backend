#!/usr/bin/env python3
"""
Flask: mdoule to run our app
Bable: configuring our flask app
"""
from flask import Flask, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

SUPPORTED_LOCALE = ['fr', 'en']
DEFAULT_LOCALE = 'en'

@babel.localeselector
def get_locale():
    """
    forces a locale on the url
    """
    locale = request.args.get('locale')

    if locale and locale in SUPPORTED_LOCALE:
        return locale
    return DEFAULT_LOCALE
