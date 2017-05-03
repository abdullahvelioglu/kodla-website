"""
Django settings for source project.

Generated by 'django-admin startproject' using Django 1.9.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Standart Library
import os
import sys

# Local Django
from .secret import (
    SECRET_KEY, GOOGLE_MAP_API_KEY,
    RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY,
    TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PACKAGE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
BASE_DIR = os.path.dirname(PACKAGE_ROOT)

sys.path.append(PACKAGE_ROOT + '/apps')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY


# Application definition

INSTALLED_APPS = [
    # Native Applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'source',

    # External Applications
    'redactor',
    'geoposition',
    'adminsortable',
    'easy_thumbnails',
    'snowpenguin.django.recaptcha2',

    # Internal Applications
    'core',
    'form',
    'activity',
    'speaker',
    'program',
    'sponsor',
    'gallery',
    'hackathon'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'source.apps.core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PACKAGE_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.static',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'source.wsgi.application'


# Django Geoposition
GEOPOSITION_GOOGLE_MAPS_API_KEY = GOOGLE_MAP_API_KEY
GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 6,
    'center': {'lat': 41, 'lng': 39.71}
}
GEOPOSITION_MARKER_OPTIONS = {
    'position': {'lat': 41, 'lng': 39.71}
}


# ReCaptcha
RECAPTCHA_PUBLIC_KEY = RECAPTCHA_PUBLIC_KEY
RECAPTCHA_PRIVATE_KEY = RECAPTCHA_PRIVATE_KEY


# Twitter
TWITTER_CONSUMER_KEY = TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET = TWITTER_CONSUMER_SECRET
TWITTER_ACCESS_TOKEN = TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET = TWITTER_ACCESS_TOKEN_SECRET


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'tr-TR'

LOCALE_PATHS = [
    os.path.join(PACKAGE_ROOT, 'locale')
]

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PACKAGE_ROOT, 'static/')


# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Easy Thumbnails
THUMBNAIL_MEDIA_URL = "/media/thumbnail/"
THUMBNAIL_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'thumbnail/')
