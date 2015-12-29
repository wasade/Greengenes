# -*- coding: utf-8 -*-
"""
    gg.manage.users
    ~~~~~~~~~~~~~~~~~~~~~
    user management commands

    adapted from:
    https://github.com/mattupstate/overholt
"""

from flask import current_app
from flask.ext.script import Command, prompt, prompt_pass
from flask_security.forms import RegisterForm
from flask_security.registerable import register_user
from werkzeug.datastructures import MultiDict

from ..services import users, apikey


class CreateAPIKeyCommand(Command):
    """Create a user"""

    def run(self):
        email = prompt('Email')
        user = users.first(email=email)
        if not user:
            print('Invalid user')
            return
        print(user.id)
        print(user.email)
        item = apikey.create(user=user, active=True)
        print(item)
