"""
Django settings for hacktrick_web_app project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from django.urls.base import reverse_lazy
from kombu import Exchange, Queue
import environ

env = environ.Env(DEBUG=(bool, False),)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, 'main', 'extra', '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'this data will be changed'

# SECURITY WARNING: don't run with debug turned on in production!
IS_DEV = True

ALLOWED_HOSTS = ['localhost', 'www.hacktrickconf.com', 'dev0001.hacktrickconf.com', '185.44.192.125', '127.0.0.1','94.55.146.209','192.168.193.227']

# Application definition
INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'hacktrick',
    'profiles',

    'social_django',
    'phonenumber_field',
    'pure_pagination',
    'django_cleanup',
    'nocaptcha_recaptcha',
    'ckeditor',
    'django_bleach',
    'hijack',
    'compat',
    'hijack_admin',
    'compressor'
]

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'main.middleware.logging.LogVariablesMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'hacktrick.context_processors.get_settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Authentication backends
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'tr-tr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/assets/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets/'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Media
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/m/"

# Grappelli
GRAPPELLI_ADMIN_TITLE = "Hacktrick Admin Panel"

# Admin
ADMINS = [('Mazlum', 'info@mazlumagar.com')]

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] [%(client_ip)s - %(user)-8s] %(levelname)s [%(name)s:%(lineno)s]  %(message)s",
        },
        'simple': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s]  %(message)s",
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/../logs/logfile",
            'maxBytes': 3145728,
            'backupCount': 150,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'hacktrick': {
            'handlers': ['logfile', 'mail_admins'],
            'level': 'DEBUG',
        },
    }
}

# Auth User
AUTH_USER_MODEL = 'profiles.Profile'

# Mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'info@oltalama.com'
EMAIL_USE_TLS = True

# Social Auth
SOCIAL_AUTH_GITHUB_KEY = env('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = env('SOCIAL_AUTH_GITHUB_SECRET')
SOCIAL_AUTH_GITHUB_SCOPE = ['user:email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details'
)

# Celery
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)

# Pagination
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10,
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

# Nocaptcha
NORECAPTCHA_SITE_KEY = env('NORECAPTCHA_SITE_KEY')
NORECAPTCHA_SECRET_KEY = env('NORECAPTCHA_SECRET_KEY')

# ADMIN URL
ADMIN_URL = env('ADMIN_PAGE_URL')
LOGIN_ERROR_URL = reverse_lazy('profiles:login_error')


# Ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'NumberedList',
        'width': 1200,
        'autoParagraph': False,
        'allowedContent': True
    },
    'filtered': {
        'toolbar': [
            ['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['NumberedList', 'BulletedList']
        ],
        'width': 800,
        'autoParagraph': False,
        'allowedContent': True,
        'format_tags': 'p;h1;h2;h3;h4;h5;h6'
    },
}
CKEDITOR_JQUERY_URL = '{}js/jquery.min.js'.format(STATIC_URL)
CKEDITOR_UPLOAD_PATH = 'uploads/'

# BLEACH
BLEACH_ALLOWED_TAGS = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'li', 'strong', 's', 'u', 'em']
BLEACH_ALLOWED_ATTRIBUTES = []
BLEACH_ALLOWED_STYLES = []
BLEACH_DEFAULT_WIDGET = 'wysiwyg.widgets.WysiwygWidget'
BLEACH_STRIP_TAGS = True
BLEACH_STRIP_COMMENTS = True

# Hijack
HIJACK_LOGIN_REDIRECT_URL = '/accounts/profile/'
HIJACK_LOGOUT_REDIRECT_URL = ADMIN_URL
HIJACK_REGISTER_ADMIN = False
HIJACK_ALLOW_GET_REQUESTS = True

# Minify and compress
HTML_MINIFY = not IS_DEV
COMPRESS_ENABLED = not IS_DEV

if IS_DEV:
    from .extra.dev_settings import *
else:
    from .extra.prod_settings import *
