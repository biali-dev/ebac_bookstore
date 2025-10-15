ARG PYTHON_VERSION=3.13-slim
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code
WORKDIR /code

RUN pip install poetry
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction
COPY . /code

# Passagem de build-arg para ENV
ARG DJANGO_ALLOWED_HOSTS
ENV DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}

ENV SECRET_KEY "R0oHkQlrWpr8ihYsI5gIqz5n5pAwVE25JxqaEk2MRkGEfXjP0D"

# Agora collectstatic vai funcionar
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn","--bind",":8000","--workers","2","bookstore.wsgi"]
