#!/usr/bin/env python

from unittest import TestCase, main
import tempfile

from greengenes.web.lib.configuration import GGConfig

class ConfigurationTests(TestCase):
    def setUp(self):
        self.config = tempfile.NamedTemporaryFile()
        self.config.write(test_config)
        self.config.seek(0)
        self.config_fp = self.config.name

    def tearDown(self):
        self.config.close()

    def test_init(self):
        GGConfig(self.config_fp)

        with self.assertRaises(IOError):
            GGConfig('does not exist')

    def test_get_main(self):
        config = GGConfig(self.config_fp)
        self.assertTrue(config.debug)

    def test_get_postgres(self):
        config = GGConfig(self.config_fp)
        self.assertEqual(config.db_user, 'test')
        self.assertEqual(config.db_password, '')
        self.assertEqual(config.db_database, 'greengenes')
        self.assertEqual(config.db_host, 'localhost')
        self.assertEqual(config.db_port, 5432)
        self.assertEqual(config.db_salt, '$123123123.')

    def test_get_tornado(self):
        config = GGConfig(self.config_fp)
        self.assertEqual(config.http_port, 8888)

    def test_get_compute(self):
        config = GGConfig(self.config_fp)
        self.assertEqual(config.compute_profile, 8888)

test_config = """[main]
debug = True

[postgres]
user = test
password =
database = greengenes
host = localhost
port = 5432
salt = $123123123.

[tornado]
port = 8888

[tornado]
profile = default
"""


if __name__ == '__main__':
    main()
