# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2011--, The Greengenes Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
    gg.apikey.models
    ~~~~~~~~~~~~~~~~~~~~~
    APIKey models
"""
from uuid import uuid4

from ..core import db, CommonMixin


class APIKey(CommonMixin, db.Model):
    __tablename__ = 'apikey'

    active = db.Column(db.Boolean(), default=False, nullable=False)
    key = db.Column(db.String(64), server_default=str(uuid4()))
    ip = db.Column(db.String(100))
    use_count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('APIKey'))
