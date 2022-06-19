build: cd backend && python manage.py collectstatic --noinput
release: cd backend && python manage.py migrate --no-input
web: cd backend && gunicorn core.wsgi:application
