# -*- coding: utf-8 -*-
"""
    wsgi
    ~~~~
    gg wsgi module

    derived from https://github.com/mattupstate/overholt
"""

from flask.ext.sqlalchemy import SQLAlchemy

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from gg import api

api_app = api.create_app()

if __name__ == "__main__":
    db = SQLAlchemy(api_app)
    db.create_all()
    run_simple('127.0.0.1', 5000, api_app, use_reloader=True,
               use_debugger=True)