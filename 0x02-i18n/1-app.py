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
    BABLE_DEFAULT_LOCALE = 'en'
    BABLE_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
bable = Bable(app)
