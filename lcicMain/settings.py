import os
from datetime import timedelta
from corsheaders.defaults import default_headers

TIME_ZONE = 'Asia/Bangkok'
USE_TZ = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
SECRET_KEY = 'django-insecure-bfz1cy+$%d8touxu*_)rath$19zbh9or8#o51t(=!7(u++1scp'
DEBUG = True
ALLOWED_HOSTS = ['*']
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
ASGI_APPLICATION = 'lcicHome.asgi.application'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'lcicHome',
    'lcicMain',
    'lcicNews',
    'ned_sql',
    'utility',
    'channels',
    "crispy_forms",
    # "crispy_bootstrap5",
    'rest_framework_simplejwt',
    'rest_framework',
    'rest_framework.authtoken',
    
]

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
#     ],
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'UID',
    'USER_ID_CLAIM': 'user_id',
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

WKHTMLTOPDF_CMD_OPTIONS = {
    'quiet': True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'lcicMain.urls'

SESSION_COOKIE_AGE = 3000

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

import pyodbc

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lcicwebsitedb',
        'USER': 'postgres', 
        'PASSWORD': 'Lcic@123',
        'HOST': '192.168.45.230',
        'PORT': '5432',
         'connect_timeout': 600,  
            'options': '-c statement_timeout=600000'  
    },
    'utility': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'utility',
        'USER': 'postgres',
        'PASSWORD': 'Lcic@123',
        'HOST': '192.168.45.230',
        'PORT': '5432',
       
    },
    'ned_sql': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'LCIC_Fingers_old',
        'USER': 'sa',
        'PASSWORD': 'Lcic@12345',
        'HOST': '192.168.45.245\EXPRESS',
        'PORT': '57004',
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
        },
    },
}


# DATABASE_ROUTERS = ['sqlserver_models.router.NEDRouter']
DATABASE_ROUTERS = ['lcicMain.db_router.DatabaseRouter']
# DATABASE_ROUTERS = [
#     'utility.db_router.UtilityDBRouter',
#     'utility.db_router.SQLServerDBRouter',
# ]

# connection_string = (
#     "DRIVER={ODBC Driver 17 for SQL Server};"
#     "SERVER=192.168.45.245\\EXPRESS,1433;"
#     "DATABASE=NED;"
#     "UID=sa;"
#     "PWD=Lcic@12345;"
# )

# try:
#     conn = pyodbc.connect(connection_string)
#     print("Connection successful!")
# except pyodbc.Error as e:
#     print("Connection failed:", e)

# from django.db import connections
# from django.db.utils import OperationalError

# def check_connection(alias):
#     try:
#         connection = connections[alias]
#         connection.cursor()
#     except OperationalError:
#         print(f"Error connecting to {alias} database")
#         return False

# check_connection('default')
# check_connection('sql_server')

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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
]

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOWED_ORIGINS = [
    "http://192.168.45.54:3000",
    "http://192.168.45.54:3000",
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-User-Roles',
]

AUTH_USER_MODEL = 'lcicHome.Login'

CSRF_TRUSTED_ORIGINS = ['http://localhost:3000','http://192.168.45.54:3000']

CORS_ALLOWED_ORIGINS = [
    "http://192.168.45.54:35729",
    # origins ອື່ນໆທີ່ມີຢູ່ແລ້ວ...
]
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = False
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
LOGIN_URL = '/accounts/login/'
CELERY_BROKER_URL = 'redis://localhost:3000/0'
CELERY_RESULT_BACKEND = 'redis://localhost:35725/0'

# Celery settings
# CELERY_BROKER_URL = 'redis://localhost:8000/0'
# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:8000/0'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CORS_ALLOW_CREDENTIALS = True
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

WATER_API_BASE_URL = 'http://202.137.141.244:3000'

DATA_UPLOAD_MAX_MEMORY_SIZE = 524288000  # 500MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 524288000  # 500MB