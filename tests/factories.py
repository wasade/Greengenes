# -*- coding: utf-8 -*-
"""
    tests.factories
    ~~~~~~~~~~~~~~~
    GG test factories module

    Adapted from:
    https://github.com/mattupstate/overholt
"""

from datetime import datetime

from factory import Sequence, LazyAttribute, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from flask_security.utils import encrypt_password

from gg.core import db
from gg.models import *


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    id = Sequence(lambda n: n)
    email = Sequence(lambda n: 'user{0}@gg.com'.format(n))
    password = LazyAttribute(lambda a: encrypt_password('password'))
    last_login_at = datetime.utcnow()
    current_login_at = datetime.utcnow()
    last_login_ip = '127.0.0.1'
    current_login_ip = '127.0.0.1'
    login_count = 1
    active = True
