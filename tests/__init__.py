# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2011--, The Greengenes Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
    tests
    ~~~~~
    tests package

    Adapted from:
    https://github.com/mattupstate/overholt
"""

from unittest import TestCase

from gg.core import db
import factory
from .factories import UserFactory
from .utils import FlaskTestCaseMixin


class GGTestCase(TestCase):
    pass


class GGAppTestCase(FlaskTestCaseMixin, GGTestCase):

    def _create_app(self):
        raise NotImplementedError

    def _create_fixtures(self):
        #with factory.debug():
        self.user = UserFactory.create()

    def setUp(self):
        super(GGAppTestCase, self).setUp()
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        from gg.services import users

        self._create_fixtures()
        self._create_csrf_token()

    def tearDown(self):
        super(GGAppTestCase, self).tearDown()
        db.drop_all()
        self.app_context.pop()

    def _login(self, email=None, password=None):
        email = email or self.user.email
        password = password or 'password'
        return self.post('/login', data={'email': email, 'password': password},
                         follow_redirects=False)
