from pathlib import Path
from os import environ
from enum import Enum
import logging


BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = environ.get("DEBUG", "False") == "True"
SECRET_KEY = environ.get("SECRET", "secret")

logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'deutsch.urls'

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

WSGI_APPLICATION = 'deutsch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'PASSWORD': environ.get("DB_PASSWORD", "root"),
        'HOST': environ.get("DB_HOST", "127.0.0.1"),
        'NAME': environ.get("DB_NAME", "testdb"),
        'USER': environ.get("DB_USER", "root"),
        'PORT': environ.get("DB_PORT", "3306"),
        'ENGINE': 'django.db.backends.mysql',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


class GROUPS(Enum):
    adjective: str = "adjective"
    pronoun: str = "pronoun"
    noun: str = "noun"
    verb: str = "verb"


class GENUSES(Enum):
    masculine: str = "masculine"
    feminin: str = "feminin"
    neutral: str = "neutral"


PRONOUN = {
    "you_many": {"rs": "ви", "ru": "вы"},
    "they": {"rs": "они", "ru": "они"},
    "you": {"rs": "ти", "ru": "ты"},
    "he": {"rs": "он", "ru": "он"},
    "we": {"rs": "ми", "ru": "мы"},
    "i": {"rs": "ја", "ru": "я"},
}
