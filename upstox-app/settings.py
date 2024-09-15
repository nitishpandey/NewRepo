"""
Django settings for upstox project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
from typing import Any



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
print(__file__)
#STATIC_ROOT = BASE_DIR / 'static'
STATIC_ROOT = os.path.join(str(BASE_DIR), 'staticcollection')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@xa*5%@cl&*xks*&*h8x(@+5y%opg-*%g@s-eu!frw&$r7dm0y'



CSRF_TRUSTED_ORIGINS = ['https://upstox-app.azurewebsites.net', 'http://localhost:3000','http://127.0.0.1:3000']
CSRF_COOKIE_SAMESITE = None
#SameSite=None
#SESSION_COOKIE_DOMAIN='127.0.0.1'
CSRF_COOKIE_HTTPONLY  = False
# Application definition
CORS_ALLOWED_ORIGINS = [

"http://127.0.0.1:3000",
 'http://localhost:3000',
 'http://0.0.0.0:4000'

]
CORS_ALLOW_CREDENTIALS = True  # Allow sending cookies in cross-origin requests
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'corsheaders',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'fnoappbe' #required to scan for templates folder 
  ]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
   ]

ROOT_URLCONF = 'upstox-app.urls'
ALLOWED_HOSTS = ['*']
#\ backslash needs to be escaped and works only on windows. For Linux need to use / and there's no need to escape it
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['upstox-app/templates'], #could not list the app in installed apps because of the hyphen
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

WSGI_APPLICATION = 'upstox-app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
 

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {  # Log to a file
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {  # Log messages from Django itself
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'upstox-app': {  # Log messages from your 'myapp' app
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}