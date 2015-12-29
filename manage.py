# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2011--, The Greengenes Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
    manage
    ~~~~~~
    Manager module

    Adapted from
    https://github.com/mattupstate/overholt
"""

from flask.ext.script import Manager

from gg.api import create_app
from gg.manage import (CreateUserCommand, DeleteUserCommand, ListUsersCommand,
                       CreateAPIKeyCommand)

manager = Manager(create_app())
manager.add_command('create_user', CreateUserCommand())
manager.add_command('create_apikey', CreateAPIKeyCommand())
manager.add_command('delete_user', DeleteUserCommand())
manager.add_command('list_users', ListUsersCommand())

if __name__ == "__main__":
    manager.run()
