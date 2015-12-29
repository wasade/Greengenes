# -*- coding: utf-8 -*-
"""
    gg.apikey
    ~~~~~~~~~~~~~~
    gg apikey package

    derived from overholt
    https://github.com/mattupstate/overholt
"""

from ..core import Service
from .models import APIKey


class APIKeyService(Service):
    __model__ = APIKey
