#!/usr/bin/env python3
"""
all are used for this task
"""
import pytz
from typing import Dict, Any
import requests
from flask_babel import Babel
from flask import Flask, g, render_template, request
from babel.dates import get_timezone, timezone_selector


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)
babel = Babel(app)

SUPPORTED_LOCALE = ['fr', 'en']
DEFAULT_LOCALE = 'fr'

@babel.localeselector
def get_locale():
    """
    forces a locale on the url
    """
    user = get_user()
    locale = users[user]["locale"]

    if locale and locale in SUPPORTED_LOCALE:
        return locale
    return DEFAULT_LOCALE

@timezone_selector
def get_timezone():
    """
    A function to get the timezone
    """
    user = get_user()
    timezone = users[user]["timezone"]
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.UnknownTimeZoneError:
            pass
    """
    user_timezone = get_user_timezone()
    if user_timezone:
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.UnknownTimeZoneError:
            pass
    """
    return 'UTC'

def get_user() -> Dict:
    """
    A function that gets the user id from the url arg
    """
    user_id = requests.args.get('login_as')
    if user_id is not None or user_id in users:
        return users[user_id]
    return None

@app.before_request
def before_request() -> Any:
    """
    the function that gets called from anyothers
    """
    get_u = get_user()
    home_header = _("Hello World!")
    if get_u is not None:
        g.user = get_u
        logged_in_as = _("You are logged in as {}.".format(users[get_u]["name"]))
        return render_template(
                '7-index.html',
                header=home_header,
                logged_in_as=logged_in_as
                )
    not_logged_in = _("You are not logged in.")

    return render_template(
            '7-index.html',
            header=home_header
            not_logged_in=not_logged_in
            )
