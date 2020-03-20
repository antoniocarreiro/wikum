"""
Django settings for wikum project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from __future__ import print_function

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.dirname(BASE_DIR)
try:
    exec(open(BASE_DIR + '/private.py').read())
except IOError:
    print("Unable to open configuration file!")


_ENV_FILE_PATH = '/opt/wikum/env'
_DEBUG_FILE_PATH = '/opt/wikum/debug'
PRAW_USERNAME = ''
PRAW_PASSWORD = ''
PRAW_CLIENT_ID = ''
PRAW_CLIENT_SECRET = ''

def _get_env():
    f = open(_ENV_FILE_PATH)
    env = f.read()

    if env[-1] == '\n':
        env = env[:-1]
    
    f.close()
    return env
ENV = _get_env() 

def _get_debug():
    f = open(_DEBUG_FILE_PATH)
    debug = f.read()

    if debug[-1] == '\n':
        debug = debug[:-1]
    
    f.close()
    if debug == 'true':
        return True
    else:
        return False
    
DEBUG = _get_debug()

if ENV == 'prod':
    BASE_URL = 'murmur.csail.mit.edu'
    MYSQL = MYSQL_PROD
elif ENV == 'staging':
    BASE_URL = 'murmur-dev.csail.mit.edu'
    MYSQL = MYSQL_DEV
else:
    BASE_URL = 'localhost:8000'
    MYSQL = MYSQL_LOCAL

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['wikum.org', '.wikum.csail.mit.edu', 'localhost', '128.52.139.135']

#database connection max age
CONN_MAX_AGE = 0

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'channels',
    'website',
    'tracking',
    'account',
    "pinax.notifications",
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'tracking.middleware.VisitorTrackingMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
    
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ROOT_URLCONF = 'wikum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n', # added this one
                'django.contrib.messages.context_processors.messages',
                'account.context_processors.account',
            ],
        },
    },
]

PINAX_NOTIFICATIONS_BACKENDS = [
    ("email", "pinax.notifications.backends.email.EmailBackend"),
]

WSGI_APPLICATION = 'wikum.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': MYSQL["NAME"],# Or path to database file if using sqlite3.
        'USER': MYSQL["USER"], # Not used with sqlite3.
        'PASSWORD': MYSQL["PASSWORD"],# Not used with sqlite3.
        'HOST': MYSQL["HOST"], # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
        'STORAGE_ENGINE': 'MyISAM / INNODB / ETC'
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# BROKER_URL = 'message_broker://user:password@hostname:port/virtual_host'
# message_broker --> rabbitmq = amqp
#BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# List of modules to import when celery starts.
#CELERY_IMPORTS = ("website.tasks",)
#CELERY_RESULT_BACKEND = "db+mysql://root:koob@localhost/celery"
#CELERY_IGNORE_RESULT = False
#CELERY_RESULT_DB_SHORT_LIVED_SESSIONS = True
#CELERY_RESULT_BACKEND = "db+mysql://celery:koob@localhost/celery"
CELERY_BROKER_URL = 'redis://localhost:6379' 
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/



LANGUAGE_CODE = 'es'

from django.utils.translation import ugettext_lazy as _

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TRACK_AJAX_REQUESTS = True
TRACK_ANONYMOUS_USERS = True
TRACK_PAGEVIEWS = True
TRACK_REFERER = True
TRACK_QUERY_STRING = True


LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)
LOCALE_PATHS = (
    BASE_DIR + '/website/locale',     
)

DEFAULT_CHARSET = 'utf-8'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join('website/static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# redis_host = os.environ.get('REDIS_HOST', 'localhost')
# Channel settings
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
    },
}

# ASGI_APPLICATION should be set to your outermost router
ASGI_APPLICATION = 'wikum.routing.application'

