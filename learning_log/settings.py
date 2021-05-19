"""
Django settings for learning_log project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'q#b78i527c&e0a@w=0wdsh@2zv%ry3!^x-*3=0#3(n@5*2xwq3'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'q#b78i527c&e0a@w=0wdsh@2zv%ry3!^x-*3=0#3(n@5*2xwq3')
# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap3',

    'learning_logs',
    'users'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'learning_log.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'learning_log.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = 'users/login/'

# Настройки django-bootstrap3
BOOTSTRAP3 = {
    'include_jquery': True,
}

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

# Настройки Heroku
if os.getcwd() == '/app':



    # Поддержка заголовка 'X-Forwarded-Proto' для request.is_secure().
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARD_PROTO', 'https')

    # Разрешены все заголовки хостов.


    # Конфигурация статических ресурсов
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)