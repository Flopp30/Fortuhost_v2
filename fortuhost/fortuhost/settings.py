import os
from pathlib import Path

from django.urls import reverse_lazy
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR.parent / ".env")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4=3k4kd3m^_og!k%l9q3451#xzoog=35!mi3@*w1g+atrqw$0('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', True)

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", '*').split(" ")

CSRF_TRUSTED_ORIGINS = os.environ.get(
    "DJANGO_CSRF_TRUSTED_ORIGINS",
    "https://fortuhost.ru"
).split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.yandex',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',

    # custom
    "user",
    "hosted_app",
    "sign",
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


ROOT_URLCONF = 'fortuhost.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'fortuhost.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DJANGO_DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("DJANGO_DB_NAME", "fortuhost"),
        "USER": os.environ.get("DJANGO_DB_USER", "admin"),
        "PASSWORD": os.environ.get("DJANGO_DB_PASSWORD", "pass"),
        "HOST": os.environ.get("DJANGO_DB_HOST", "localhost"),
        "PORT": os.environ.get("DJANGO_DB_PORT", "5435"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_USER_MODEL = "user.User"

LOGIN_REDIRECT_URL = reverse_lazy("hosted_app:list")

LOGOUT_REDIRECT_URL = reverse_lazy("index")

# TODO need to delete it when need to send emails again
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
# end remove area

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

USE_L10N = False

SHORT_DATE_FORMAT = "Y.m.d"
DATE_FORMAT = SHORT_DATE_FORMAT
TIME_FORMAT = "H:i:s"
DATETIME_FORMAT = f"{DATE_FORMAT} {TIME_FORMAT}"
SHORT_DATETIME_FORMAT = f"{SHORT_DATE_FORMAT} H:i"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_DIR = BASE_DIR / 'static'
# STATIC_ROOT = os.path.join(BASE_DIR, '')

STATICFILES_DIRS = [
    STATIC_DIR,
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, '')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {name} | {filename}>{funcName}():{lineno} | {message}',
            'style': '{',
        },
        'simple': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'filters': ['require_debug_false']
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.environ.get('DEBUG_LOG', './django-debug.log'),
            'filters': ['require_debug_true']
        },
        'errors_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.environ.get('ERROR_LOG', './django-error.log'),
            'when': 'MIDNIGHT',
            'backupCount': 7,
            'formatter': 'verbose',
        },
        'base_log': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.environ.get('BASE_LOG', './django-base.log'),
            'when': 'MIDNIGHT',
            'backupCount': 7,
            'formatter': 'verbose',
        },
        'base_log_warning': {
            'level': 'WARNING',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.environ.get('BASE_LOG', './django-base.log'),
            'when': 'MIDNIGHT',
            'backupCount': 7,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['console', 'errors_file', 'base_log'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django': {
            'handlers': ['mail_admins', 'console', 'errors_file', 'base_log'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': True,
        },
        'django.server': {
            'level': 'INFO',
            'handlers': ['console', 'base_log_warning'],
            'propagate': False,
        },
        '': {
            'level': 'INFO',
            'handlers': ['console', 'base_log', 'errors_file'],
            'propagate': True,
        }
    }
}

if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1"]

    LOGGING['handlers']['errors_file'] = {
        'class': 'logging.NullHandler',
    }
    LOGGING['handlers']['base_log'] = {
        'class': 'logging.NullHandler'
    }
    LOGGING['handlers']['base_log_warning'] = {
        'class': 'logging.NullHandler'
    }
    LOGGING['handlers']['debug_file'] = {
        'class': 'logging.NullHandler'
    }

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
