#!/usr/bin/env python3
"""
Flask: mdoule to run our app
Bable: configuring our flask app
"""
from flask import Flask, request
from flask_bable import Bable


class Config():
    """
    Config class to configure our bable and flask app
    Attributes:
        LANGUAGES - supported languages for this app
        BABLE_DEFAULT_LOCALE - setting default value to local
        BABLE_DEFAULT_TIMEZONE - setting the default timezone
    """
    LANGUAGES = ["en", "fr"]
    BABLE_DEFAULT_LOCALE = 'en'
    BABLE_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
bable = Bable(app)

@bable.localeselector
def get_locale():
    """
    gets the best match local language based on the
    supported
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
