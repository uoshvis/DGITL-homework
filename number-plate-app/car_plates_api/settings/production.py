from .base import *
from settings_secret import DB_PASS, DB_HOST, DB_USER, DB_NAME

DEBUG = False
ALLOWED_HOSTS += ['uoshvis.pythonanywhere.com', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'HOST': DB_HOST,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

SECURE_SSL_REDIRECT = True
