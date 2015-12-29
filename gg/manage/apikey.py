# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2011--, The Greengenes Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
    gg.manage.users
    ~~~~~~~~~~~~~~~~~~~~~
    user management commands

    adapted from:
    https://github.com/mattupstate/overholt
"""

from flask.ext.script import Command, prompt

from ..services import users, apikey


class CreateAPIKeyCommand(Command):
    """Create a user"""

    def run(self):
        email = prompt('Email')
        user = users.first(email=email)
        if not user:
            print('Invalid user')
            return
        item = apikey.create(user=user, active=True)
        print(item.key)
