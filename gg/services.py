# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2011--, The Greengenes Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
    gg.services
    ~~~~~~~~~~~~~~~~~
    services module

    derived from overholt
    https://github.com/mattupstate/overholt
"""

from .users import UsersService
from .apikey import APIKeyService
from .record import RecordService

users = UsersService()
apikey = APIKeyService()
record = RecordService()
