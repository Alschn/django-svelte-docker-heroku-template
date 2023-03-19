ARG PYTHON_VERSION=3.11.2-alpine

# Make pipenv available in each step
FROM python:${PYTHON_VERSION} as base
RUN  \
    apk update && \
    apk upgrade && \
    pip3 install pipenv --force-reinstall

# Build stage
FROM base as build-image

ENV PYTHONUNBUFFERED=1
ENV PIPENV_VENV_IN_PROJECT=1

COPY Pipfile .

# Install packages only needed in build stage
RUN  \
    apk add --virtual .build-deps gcc musl-dev postgresql-libs postgresql-dev && \
    pipenv install --dev --deploy --python 3.11 && \
    apk --purge del .build-deps

# Run stage
FROM base as runtime

ENV PYTHONUNBUFFERED=1

# Copy .venv from build stage
COPY --from=build-image /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Install packages that are only needed runtime
RUN  \
    apk add bash postgresql-libs && \
    rm -rf /var/cache/apk/*

# Add the rest of the code
COPY . /app/backend
COPY ./scripts/ /app/

# Make port 8000 available for the app
ENV PORT 8000
EXPOSE 8000

# Change directory so that scripts could locate manage.py
WORKDIR /app/backend

# Be sure to use 0.0.0.0 for the host within the Docker container,
# otherwise the browser won't be able to find it
RUN ["chmod", "+x", "/app/entrypoint-dev.sh"]
ENTRYPOINT [ "/app/entrypoint-dev.sh" ]
