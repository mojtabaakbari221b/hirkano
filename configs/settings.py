"""
Django settings for hirkano project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from .utilities import load_env

env = load_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG') == 'True'

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')
CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',

    'constance',
    'constance.backends.database',
    'widget_tweaks',

    'hirkano.blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

SITE_ID = 1

ROOT_URLCONF = 'configs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'hirkano/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'configs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if env('USE_SQLITE') == 'True':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('POSTGRES_DB'),
            'USER': env('POSTGRES_USER'),
            'PASSWORD': env('POSTGRES_PASSWORD'),
            'HOST': env('POSTGRES_HOST'),
            'PORT': env('POSTGRES_PORT'),
        }
    }



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'hirkano/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'hirkano/media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CONSTANCE settings

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': [
        'django.forms.ImageField',
        {},
    ]
}

CONSTANCE_CONFIG = {
    'CONTACT_US_ADDRESS': (
        'Babol, Noshirvani Uni', 
        'address of your place.',
    ),
    'CONTACT_US_NUMBER': (
        '+981134704856', 
        'number of your place.',
    ),
    'CONTACT_US_EMAIL': (
        'contact@inolinx.com', 
        'email of your place.',
    ),
    'CONTACT_US_WEBSITE': (
        'inolinx.com', 
        'website of your place.',
    ),
    'YEARS_OF_EXPERIENCE': (
        2, 
        'years of experience.',
    ),
    'ABOUT_LOGO': (
        'default.png',
        'about us logo',
        'image_field',
    ),
    'SERVICES_LOGO': (
        'default.png',
        'services logo',
        'image_field',
    ),

}