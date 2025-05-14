import os
from pathlib import Path
from dotenv import dotenv_values

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ENV = dotenv_values(BASE_DIR / '.env')

SECRET_KEY = ENV.get('SECRET_KEY')

ALLOWED_HOSTS = ["*"]

CUSTOM_APPS = [
    "apps.chat",
]


SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# THIRD_PARTY_APPS = [
# ]

INSTALLED_APPS = CUSTOM_APPS + SYSTEM_APPS

# Channels 환경세팅##################
INSTALLED_APPS += ['channels']
ASGI_APPLICATION = 'config.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        }
    }
}
###################################


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
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


# DB setting######################
DATABASES = {
    'default': {
        'ENGINE': ENV.get('DB_ENGINE'),
        'NAME': ENV.get('DB_NAME'),
        'USER': ENV.get('DB_USER'),
        'PASSWORD': ENV.get('DB_PASSWORD'),
        'HOST': ENV.get('DB_HOST'),
        'PORT': ENV.get('DB_PORT'),
    }
}
##################################


# Internationalization
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Swagger settings#############
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    # JWT 토큰 활성화 후 적용
    # 'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication',],
    # 'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated',],
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'Study_Bugs',
    'DESCRIPTION': 'Study_Bugs',
    'VERSION': '1.0.0',
    'COMPONENT_SPLIT_REQUEST': True,  # 요청과 응답 스키마 분리
    'SERVE_INCLUDE_SCHEMA': False,  # 스키마 엔드포인트를 포함하지 않도록 설정
}   # '/api/schema/' 숨김처리
################################



# LOGGING Setting############################
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "console.info": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
        },
        "console.error": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
        },
        "logger.info": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "logger.warning": {
            "level": "WARNING",
            "handlers": ["console"],
            "propagate": False,
        },
        "logger.error": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}
#######################################