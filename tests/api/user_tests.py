# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2011--, The Greengenes Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
    tests.api.user_tests
    ~~~~~~~~~~~~~~~~~~~~
    api user tests module

    Adapted from:
    https://github.com/mattupstate/overholt
"""

from flask.json import loads

from . import GGApiTestCase


class UserApiTestCase(GGApiTestCase):

    def test_get_current_user(self):
        r = self.jget('/users')
        self.assertOkJson(r)
        self.assertIn(self.user.id, loads(r.data)['data'])

    def test_get_user(self):
        r = self.jget('/users/%s' % self.user.id)
        self.assertOkJson(r)
        self.assertEqual(loads(r.data)['data']['email'], self.user.email)
