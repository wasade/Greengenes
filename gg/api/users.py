# -*- coding: utf-8 -*-
"""
    gg.api.users
    ~~~~~~~~~~~~~~~~~~
    User endpoints

    Derived from overholt:
    https://github.com/mattupstate/overholt
"""

from flask import Blueprint
from flask_login import current_user

from ..services import users
from . import route, require_appkey

bp = Blueprint('users', __name__, url_prefix='/users')


@route(bp, '/')
#@require_appkey
def whoami():
    """Returns the user instance of the currently authenticated user."""
    return [u.id for u in users.all()]


@route(bp, '/<user_id>')
def show(user_id):
    """Returns a user instance."""
    print(users.get_or_404(user_id))
    return users.get_or_404(user_id)
