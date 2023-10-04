# Creating a python base with core environment variables
FROM python:3.11-slim-bullseye as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.3.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_HOME="/opt/poetry"

# Add poetry to path to use the "poetry" command
ENV PATH="$POETRY_HOME/bin:$PATH"

# builder-base is used to build dependencies
FROM python-base as builder-base

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    # deps for installing poetry
    curl \
    # deps for dev convenience
    iputils-ping build-essential unzip

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python -

# development
FROM builder-base as development

ENV VIRTUAL_ENV=/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


COPY ecoissue /src/

WORKDIR /src

#CMD ["uvicorn", "--factory", "ecoissue.main:webapp"]
