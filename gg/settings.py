# -*- coding: utf-8 -*-
"""
    gg.settings
    ~~~~~~~~~~~~~~~
    gg settings module

    derived from:
    https://github.com/mattupstate/overholt
"""

DEBUG = True
SECRET_KEY = b'super-secret-key'

SQLALCHEMY_DATABASE_URI = 'postgresql:///ggrest'

MAIL_DEFAULT_SENDER = 'mcdonadt@colorado.edu'
MAIL_SERVER = 'smtp.postmarkapp.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'

SECURITY_POST_LOGIN_VIEW = '/'
SECURITY_PASSWORD_HASH = 'plaintext'
SECURITY_PASSWORD_SALT = 'password_salt'
SECURITY_REMEMBER_SALT = 'remember_salt'
SECURITY_RESET_SALT = 'reset_salt'
SECURITY_RESET_WITHIN = '5 days'
SECURITY_CONFIRM_WITHIN = '5 days'
SECURITY_SEND_REGISTER_EMAIL = False
