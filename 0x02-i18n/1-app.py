#!/usr/bin/env python3
"""
Flask: mdoule to run our app
Bable: configuring our flask app
"""
from flask import Flask, render_template
from flask_bable import Bable
from pytz import timezone


class Config():
    """
    Config class to configure our bable and flask app
    """
    LANGUAGES = ["en", "fr"]
    utc = pytz.utc

app = Flask(__name__)
bable = Bable(app, default_locale = Config.LANGUAGES[0], default_timezone = Config.utc.zone)


@app.route('/')
def index():
    """
    """
    return render_template('1-index.html')
