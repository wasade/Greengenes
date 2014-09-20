#!/usr/bin/env python

from redis import Redis
from IPython.parallel import Client

from greengenes.web.lib.configuration import GGConfig
from greengenes.db import GreengenesDB


config = GGConfig()
db = GreengenesDB(config.db_host, config.db_user, config.db_password,
                  False, config.db_database, config=config)
r_server = Redis()


#try:
#    parallel_client = Client(profile=config.compute_profile)
#    parallel_view = parallel_client.load_balanced_view()
#except IOError:
#    raise IOError("It doesn't look like a cluster is running!")
#
#with parallel_client[:].sync_imports(quiet=True):
#    import t2t.cli as t2tcli


__all__ = ['config', 'db', 'r_server']# 'parallel_client', 'parallel_view']
