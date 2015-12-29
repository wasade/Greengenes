# -*- coding: utf-8 -*-
"""
    gg.users
    ~~~~~~~~~~~~~~
    gg users package

    derived from overholt
    https://github.com/mattupstate/overholt
"""

from ..core import Service
from .models import User


class UsersService(Service):
    __model__ = User
