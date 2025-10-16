ARG PYTHON_VERSION=3.13-slim
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Dependências para psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# Instala poetry
RUN pip install poetry

# Copia arquivos de dependências
COPY pyproject.toml poetry.lock /code/

RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction

# Copia todo o projeto Django
COPY . /code/

# Coleta os static files
RUN python manage.py collectstatic --noinput

# Define SECRET_KEY de ambiente para produção
ENV SECRET_KEY "R0oHkQlrWpr8ihYsI5gIqz5n5pAwVE25JxqaEk2MRkGEfXjP0D"

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "bookstore.wsgi"]
