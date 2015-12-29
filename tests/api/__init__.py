# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2011--, The Greengenes Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
    tests.api
    ~~~~~~~~~
    api tests package

    Adapted from:
    https://github.com/mattupstate/overholt
"""

from gg.api import create_app

from .. import GGAppTestCase, settings


class GGApiTestCase(GGAppTestCase):

    def _create_app(self):
        return create_app(settings, reg_sec_blueprint=True)

    def setUp(self):
        super(GGApiTestCase, self).setUp()
        self._login()
