ARG PYTHON_VERSION=3.13-slim
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction

COPY . /code/

# Remova o collectstatic do build
# Será executado no entrypoint ou CMD

CMD python manage.py collectstatic --noinput && \
    gunicorn --bind :8000 --workers 2 bookstore.wsgi
