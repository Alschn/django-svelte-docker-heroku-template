# Production Dockerfile

ARG PYTHON_VERSION=3.11.2-alpine
ARG NODE_VERSION=16.16.0-alpine

FROM python:${PYTHON_VERSION} as base-python
RUN  \
    apk update && \
    apk upgrade && \
    pip3 install pipenv --force-reinstall

FROM base-python as compile-image

ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1

COPY ./backend/Pipfile ./backend/Pipfile.lock ./

RUN  \
    apk add --virtual .build-deps gcc musl-dev postgresql-libs postgresql-dev && \
    pipenv install --deploy --python 3.11 && \
    apk --purge del .build-deps

FROM node:${NODE_VERSION} as node-build

ENV DOCKER true

WORKDIR /app/frontend

COPY frontend .

RUN \
    npm i -g pnpm && \
    pnpm install --frozen-lockfile && \
    pnpm run build && \
    rm -rf node_modules


FROM base-python as runtime

ENV PYTHONUNBUFFERED 1

COPY --from=compile-image /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

WORKDIR /app/backend

RUN \
    apk add bash postgresql-libs && \
    rm -rf /var/cache/apk/*

COPY backend .

ENV DJANGO_SETTINGS_MODULE core.settings.build

COPY --from=node-build /app/frontend/build /app/backend/core/static/frontend

RUN mkdir -p staticfiles && python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "core.wsgi"]
