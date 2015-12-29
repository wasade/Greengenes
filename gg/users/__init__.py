# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2011--, The Greengenes Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
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
