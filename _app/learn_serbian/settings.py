"""
Django settings for learn_serbian project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import sys
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOCALE_PATHS = [
    'locale/',
]

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False) == 'true'

# Enable traffic and form submissions from localhost and PROD_HOST_NAME


PROD_HOST_NAME = os.getenv('PROD_HOST_NAME', None)
FRONTEND_HOST = os.getenv('FRONTEND_HOST')

ALLOWED_HOSTS = [
    PROD_HOST_NAME
]

if DEBUG:
    CSRF_TRUSTED_ORIGINS = [
        FRONTEND_HOST,
        PROD_HOST_NAME,
    ]
else:
    CSRF_TRUSTED_ORIGINS = [
        f'https://{FRONTEND_HOST}',
        f'https://{PROD_HOST_NAME}',
    ]

if not DEBUG:
    GOOGLE_CALLBACK_URL = f'https://{FRONTEND_HOST}'
else:
    GOOGLE_CALLBACK_URL = f'http://{FRONTEND_HOST}'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "whitenoise.runserver_nostatic",
    'django.contrib.sites',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'djoser',
    'accounts',
    'words',
    'topics',
    'ai',
    'learning',
    'achievements',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'dj_rest_auth.registration',

]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.getenv('GOOGLE_CLIENT_ID'),
            "secret": os.getenv('GOOGLE_CLIENT_SECRET'),
            "key": "",
        },
        'SCOPE': ['openid', 'email', 'profile'],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        },
        'INIT_PARAMS': {
            'prompt': 'consent',
        },
        # "VERIFIED_EMAIL": True,
    },
}
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_QUERY_EMAIL = True

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'learn_serbian.urls'

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

WSGI_APPLICATION = 'learn_serbian.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_USER'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
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

STATIC_URL = 'static/'
STATIC_ROOT = 'static'
# See http://whitenoise.evans.io/en/latest/django.html#enable-whitenoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redis cache support
# https://docs.djangoproject.com/en/4.0/topics/cache/#redis-1

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
    }
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
AUTH_USER_MODEL = 'accounts.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

CORS_ALLOW_ALL_ORIGINS = True

# Optional: You can customize other CORS settings as needed
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'Accept',
    'Accept-Language',
    'Content-Type',
    'Authorization',
]

MEDIA_ROOT = os.getenv('MEDIA_ROOT')
MEDIA_URL = os.getenv('MEDIA_URL')

# todo make another logger fo api
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        'std_err': {
            'class': 'logging.StreamHandler'
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            'filename': os.path.join(BASE_DIR, 'log/log.log'),
            "formatter": "verbose",
        },
        "index_logger": {
            "level": "INFO",
            "class": "logging.FileHandler",
            'filename': os.path.join(BASE_DIR, 'log/index_log.log'),
            "formatter": "verbose",
        },
        "openai_report": {
            "level": "INFO",
            "class": "logging.FileHandler",
            'filename': os.path.join(BASE_DIR, 'log/openai_info.log'),
            "formatter": "verbose",
        },
        "openai_error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            'filename': os.path.join(BASE_DIR, 'log/openai_error.log'),
            "formatter": "verbose",
        }
    },
    "loggers": {
        'openai': {
            'handlers': ['openai_error', 'openai_report'],
            'level': 1,
            'propagate': False,
        },
        'index_logger': {
            'handlers': ['index_logger'],
            'propagate': False,
        },
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
S3_SECRET_ACCESS_KEY = os.getenv('S3_SECRET_ACCESS_KEY')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
S3_REGION = os.getenv('S3_REGION')


WORDS_PER_ITERATION = 6
REPETITIONS_TO_COMPLETE = 5

MEILISEARCH_URL = os.getenv('MEILISEARCH_URL')
MEILI_MASTER_KEY = os.getenv('MEILI_MASTER_KEY')


DJOSER = {
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {
        'user_create': 'accounts.serializers.CustomUserCreateSerializer',
    },
}
