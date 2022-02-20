<div align="center" style="padding-bottom: 20px">
    <h1>Django + Svelte + Postgres + Docker + Heroku template - WIP</h1>
    <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00" alt=""/>
    <img src="https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Docker-008FCC?style=for-the-badge&logo=docker&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" alt=""/>
</div>

...

### Why Svelte rendered in Django templates?

...

### How does it work?

...

### Tools, libraries, frameworks:

This setup has been tested with Python 3.9 and Node 14.

### Backend

- Django + Django Rest Framework `django` `djangorestframework`
- `django-extensions` - useful utilities (e.g better shell)
- `django-cors-headers` - handling cross origin requests
- `coverage` - for code coverage reports and running unit tests
- `mypy` + `djangorestframework-stubs` - for better typing experience
- `psycopg2` - needed to use Postgres (in Docker container)
- `gunicorn` - production wsgi http server
- `whitenoise` - building static files

Suggested packages:

- `drf-yasg` - open api documentation (swagger and redoc) - if using DRF
- `django-rest-auth`, `django-allauth`, `djoser` - making auth easier
- `django-filter` - enables filtering querysets with url parameters and more
- `django-ninja` - API framework similar to Fast API but tied with Django
- `pipenv`, `poetry` - replacement for venv/virtualenv
- `pytest` - alternative to built-in unittest
- `selenium` - for e2e testing

### Frontend

- Svelte `svelte`
- Typescript `typescript` (not yet)
- `sass` - enables scss/sass support
- `axios` - for making requests
- `jest`, `@testing-library/svelte` + additional packages - unit testing components

Suggested packages:

- UI libraries such as `TailwindCSS`, `Svelte Material UI`, `Smelte`, `Carbon Components Svelte`, `Svelte Materialify`, `Sveltestrap` etc.
- `cypress` - for e2e testing

# Development setup

## Without Docker

### Backend

Create a virtual environment from cmd (or do it in Pycharm manually)

```shell script
cd backend

python -m venv venv

venv/Scripts/Activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

Run django application from cmd (or add new Django configuration if using Pycharm)

```shell script
python manage.py runserver
```

Preparing (if there are any changes to db schema) and running migrations

```shell script
python manage.py makemigrations

python manage.py migrate
```

Create superuser

```shell script
python manage.py createsuper user
```

### Frontend

Install node dependencies. You may use npm instead of yarn if you wish.

```shell script
cd frontend

yarn install
```

Run development server in second terminal

```shell script
yarn dev
```

### Backend tests coverage

```shell script
cd backend
```

Run tests using Coverage instead of `python manage.py test`

```shell script
coverage run manage.py test
```

Get report from coverage:

```shell script
coverage report -m
```

# TO DO:

- Dockerfiles, docker-compose.yml, scripts
- Github Actions
- Svelte with Typescript
- Svelte unit tests
- Some examples (django + svelte connection) and description
- Production settings
- Deployment to Heroku
- Frontend section in README (testing, additional info)
