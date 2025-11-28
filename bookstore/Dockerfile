FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction

COPY . /code/

CMD sh -c "python manage.py collectstatic --noinput && python manage.py migrate && gunicorn bookstore.wsgi --bind 0.0.0.0:${PORT:-8000}"
