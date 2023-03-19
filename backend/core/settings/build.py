from django.core.management.utils import get_random_secret_key
from .base import *

SECRET_KEY = get_random_secret_key()

DEBUG = False

ALLOWED_HOSTS = []

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
