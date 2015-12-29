# -*- coding: utf-8 -*-
"""
    gg.apikey.models
    ~~~~~~~~~~~~~~~~~~~~~
    APIKey models

    derived from overholt
    https://github.com/mattupstate/overholt
"""

from uuid import uuid4

from flask_security import UserMixin, RoleMixin

from ..core import db, CommonMixin


class APIKey(CommonMixin, db.Model):
    __tablename__ = 'apikey'

    active = db.Column(db.Boolean())
    key = db.Column(db.String(64), server_default=str(uuid4()))
    last_ip = db.Column(db.String(100))
    current_ip = db.Column(db.String(100))
    use_count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('APIKey'))
