# -*- coding: utf-8 -*-

import logging
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True
APPEND_SLASH = True

GoogleShortUrlApi = "AIzaSyCKBoWT8Nycyp4X6XWYnS27_wV6jKS9PPc"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paylas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'paylas.middleware.NeredeNelerOluyorMiddleware'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + "/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.request",
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ["*"]
ADMINS = (('Muslu', 'muslu.yuksektepe@makdos.com'),)
MANAGERS = ADMINS
LANGUAGE_CODE = 'tr_TR'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = False
USE_TZ = False
WSGI_APPLICATION = 'djiki.wsgi.application'

STATIC_URL = '/static/'
# STATIC_ROOT             = BASE_DIR + "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

SECRET_KEY = '9=y%oAIzaSyCKBoWT8Nycyp4X6XWYnS27_wV6jKS9PPc'
ROOT_URLCONF = 'djiki.urls'

logging.basicConfig(level=logging.INFO, format='%(message)s', filename='/home/musluyuksektepe/PycharmProjects/djangoLog.log', )
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'log_to_stdout': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        },
    },
    'loggers': {
        'main': {
            'handlers': ['log_to_stdout'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
