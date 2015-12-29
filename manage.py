# -*- coding: utf-8 -*-
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
