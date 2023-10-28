FROM python:3.9

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

# Update and install necessary packages
RUN apt update -y && apt-get install -y \
    build-essential libffi-dev libssl-dev libffi-dev \
    python3-dev cargo pkg-config

RUN pip install cryptography==3.4.6

# Optionally, set a working directory
WORKDIR /app

LABEL maintainer="Paweł Polski <harcownikapp@gmail.com>"


# Install Poetry

RUN pip --no-cache-dir install poetry

COPY ./src ./src
COPY ./alembic/ ./alembic
COPY ./pyproject.toml  .
COPY ./alembic.ini .
COPY ./entrypoint.sh .
COPY ./backend_test_connection.py .
COPY ./initial_data.py .

RUN poetry install --no-root
RUN poetry config virtualenvs.create false

RUN chmod +x ./entrypoint.sh