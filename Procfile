release: cd backend && python manage.py migrate --no-input
web: cd backend && gunicorn core.wsgi:application
