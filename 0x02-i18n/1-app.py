#!/usr/bin/env python3
"""
Flask: mdoule to run our app
Bable: configuring our flask app
"""
from flask import Flask
from flask_bable import Bable


app = Flask(__name__)
bable = Bable(app, default_locale = 'en', default_timezone = 'UTC')

class Config():
    """
    Config class to configure our bable and flask app
    """
    LANGUAGES = ["en", "fr"]
