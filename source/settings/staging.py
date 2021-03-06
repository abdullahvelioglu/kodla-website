# Local Django
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []


ADMINS = (
    # ("Your Name", "your_email@example.com"),
)


# App used only at development
INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)


MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kodladb',
        'USER': 'kodla',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': '',
    }
}


from .extra import *
