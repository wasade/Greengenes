# -*- coding: utf-8 -*-
"""
    gg.services
    ~~~~~~~~~~~~~~~~~
    services module

    derived from overholt
    https://github.com/mattupstate/overholt
"""

from .users import UsersService

from .apikey import APIKeyService

users = UsersService()
apikey = APIKeyService()
