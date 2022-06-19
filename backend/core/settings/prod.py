"""
Configuration for deployment to Heroku with Dockerfile.prod
"""
import dj_database_url
from core.settings.base import *

# project directory
ROOT_DIR = BASE_DIR.parent.parent

# set SECRET_KEY for production
SECRET_KEY = os.environ.get('SECRET_KEY')

# add heroku app url or create env var with url
ALLOWED_HOSTS = [os.environ.get("PRODUCTION_HOST")]

# debug has to be false in production
DEBUG = False

# cors headers configuration
CORS_ALLOW_ALL_ORIGINS = False

# not used in production
INSTALLED_APPS.insert(1, "whitenoise.runserver_nostatic")

# whitenoise middle - has to be first in the list
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# type of static files storage
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# directory to which Django will move those static assets and from which it will serve them when the app is running
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"

# database url set at env variable in Heroku
DATABASE_URL = os.environ.get('DATABASE_URL')

# directory where WhiteNoise can find all non-html static assets
WHITENOISE_ROOT = os.path.join(BASE_DIR, "core", "static", "frontend")

# db config
db_from_env = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=500, ssl_require=True
)

DATABASES['default'].update(db_from_env)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
                       'pathname=%(pathname)s lineno=%(lineno)s '
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
