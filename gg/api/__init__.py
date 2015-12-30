# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2011--, The Greengenes Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
    gg.api
    ~~~~~~~~~~~~~
    gg api application package

    structure derived from overholt:
    https://github.com/mattupstate/overholt/
"""

from functools import wraps

from flask import jsonify, request, abort
from flask_security import login_required

from ..core import GGError, GGFormError
from ..helpers import JSONEncoder
from .. import factory
from ..services import apikey


def create_app(settings_override=None, reg_sec_blueprint=False):
    """Returns the Greengenes API application instance"""

    app = factory.create_app(__name__, __path__, settings_override,
                             register_security_blueprint=reg_sec_blueprint)

    # Set the default JSON encoder
    app.json_encoder = JSONEncoder

    # Register custom error handlers
    app.errorhandler(GGError)(on_gg_error)
    app.errorhandler(GGFormError)(on_gg_form_error)
    app.errorhandler(404)(on_404)

    return app


def get_apikey_object_by_key(key):
    """
    Query the datastorage for an API key.
    @param ip: ip address
    @return: apikey sqlachemy object.

    adapted from: http://stackoverflow.com/a/24705557
    """
    return apikey.find(key=key, active=True).first()


def match_api_key(key, ip):
    """
    Match API keys and discard ip
    @param key: API key from request
    @param ip: remote host IP to match the key.
    @return: boolean

    adapted from: http://stackoverflow.com/a/24705557
    """
    if key is None or ip is None:
       return False

    api_key = get_apikey_object_by_key(key)

    if api_key is None:
       return False

    elif api_key.key == key and (api_key.ip == ip or api_key.ip == "0.0.0.0"):
       return True

    return False


# The actual decorator function
def require_appkey(f):
    # adapted from
    # https://coderwall.com/p/4qickw/require-an-api-key-for-a-route-in-flask-using-only-a-decorator
    # and
    # http://stackoverflow.com/a/24705557
    @wraps(f)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        if match_api_key(request.args.get('key'), request.remote_addr):
            return f(*args, **kwargs)
        else:
            abort(401)
    return decorated_function


def route(bp, *args, **kwargs):
    kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            sc = 200
            rv = f(*args, **kwargs)
            if isinstance(rv, tuple):
                sc = rv[1]
                rv = rv[0]
            return jsonify(dict(data=rv)), sc
        return f

    return decorator


def on_gg_error(e):
    return jsonify(dict(error=e.msg)), 400


def on_gg_form_error(e):
    return jsonify(dict(errors=e.errors)), 400


def on_404(e):
    return jsonify(dict(error='Not found')), 404
