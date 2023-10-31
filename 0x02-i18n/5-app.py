#!/usr/bin/env python3
"""
"""
from typing import Dict, Any
import requests
from flask import Flask, g, render_template
from 4-app import get_locale


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)

def get_user() -> Dict:
    """
    """
    user_id = requests.args.get('login_as')
    if user_id is not None or user_id in users:
        return users[user_id]
    return None

@app.before_request
def before_request() -> Any:
    """
    """
    get_u = get_user()
    home_header = _("Hello World!")
    if get_u is not None:
        g.user = get_u
        logged_in_as = _("You are logged in as {}.".format(users[get_u]["name"]))
        return render_template(
                '5-index.html',
                header=home_header,
                logged_in_as=logged_in_as
                )
    not_logged_in = _("You are not logged in.")

    return render_template(
            '5-index.html',
            header=home_header
            not_logged_in=not_logged_in
            )
