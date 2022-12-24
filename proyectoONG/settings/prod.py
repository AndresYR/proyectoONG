from .base import *

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'proyectoONG',
            'USER': 'root',
            'PASSWORD': '36390sql',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }