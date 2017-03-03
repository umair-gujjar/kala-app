"""
Django settings for django_kala project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from .apps import INSTALLED_APPS
from .authentication import *
from .basecamp import BASECAMP
from .databases import DATABASES
from .email import *
from .functions import get_env_variable
from .middleware import MIDDLEWARE
from .templates import TEMPLATES
from .validators import AUTH_PASSWORD_VALIDATORS
from .debug import *


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(e^h^f=)*li=uq3@u(965ghns0f1sd@v(i8hrc12d#0*-cnedu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

ROOT_URLCONF = 'django_kala.urls'

WSGI_APPLICATION = 'django_kala.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = '/tmp/kala/'