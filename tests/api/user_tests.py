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

from . import GGApiTestCase


class UserApiTestCase(GGApiTestCase):

    def test_get_current_user(self):
        r = self.jget('/users')
        self.assertOkJson(r)

    def test_get_user(self):
        r = self.jget('/users/%s' % self.user.id)
        self.assertOkJson(r)
