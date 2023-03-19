"""
Configuration for deployment to Fly.io with Dockerfile.prod
"""
import dj_database_url
from core.settings.base import *

ROOT_DIR = BASE_DIR.parent.parent

# set SECRET_KEY for production
SECRET_KEY = os.environ['SECRET_KEY']

# add heroku app url or create env var with url
ALLOWED_HOSTS = [
    os.environ["PRODUCTION_HOST"]
]

# debug has to be false in production
DEBUG = False

# cors headers configuration
CORS_ALLOW_ALL_ORIGINS = False

# whitenoise middle - has to be first in the list
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# type of static files storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# directory to which Django will move those static assets and from which it will serve them when the app is running
STATIC_ROOT = os.path.join(ROOT_DIR, "staticfiles")

STATIC_URL = "/static/"

# database url set at env variable in Fly.io
DATABASE_URL = os.environ['DATABASE_URL']

# db config
db_from_env = dj_database_url.config(
    default=DATABASE_URL,
    conn_max_age=500,
    ssl_require=True
)

DATABASES['default'].update({
    **db_from_env,
    "ENGINE": "django.db.backends.postgresql",
    "OPTIONS": {
        "connect_timeout": 5,
    }
})

CSRF_TRUSTED_ORIGINS = [
    "https://" + os.environ['PRODUCTION_HOST'],
]
