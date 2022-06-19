from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY', 'development')

DEBUG = True

ALLOWED_HOSTS = ["backend", "localhost", "127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'postgres'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_USER', 'postgres'),
        'HOST': os.environ.get('DB_HOST', 'postgres_db'),
        'PORT': os.environ.get('DB_PORT', 5432)
    }
}
