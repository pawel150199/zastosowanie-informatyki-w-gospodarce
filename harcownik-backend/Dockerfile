FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

LABEL maintainer="Paweł Polski <harcownikapp@gmail.com>"

WORKDIR /app

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
