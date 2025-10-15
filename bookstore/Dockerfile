# Dockerfile para Fly.io - Django
ARG PYTHON_VERSION=3.13-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Define diretório do projeto
WORKDIR /code

# Instala poetry
RUN pip install poetry

# Copia apenas arquivos de dependências primeiro
COPY pyproject.toml poetry.lock /code/

# Configura poetry para não criar virtualenv
RUN poetry config virtualenvs.create false

# Instala dependências do projeto
RUN poetry install --only main --no-root --no-interaction

# Copia todo o projeto Django
COPY . /code/

# Define SECRET_KEY de ambiente para produção
ENV SECRET_KEY "R0oHkQlrWpr8ihYsI5gIqz5n5pAwVE25JxqaEk2MRkGEfXjP0D"

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expõe porta
EXPOSE 8080

# Comando padrão para iniciar o Gunicorn
CMD ["gunicorn","--bind",":8080","--workers","2","bookstore.wsgi"]
