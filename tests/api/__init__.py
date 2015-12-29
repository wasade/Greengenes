# -*- coding: utf-8 -*-
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
