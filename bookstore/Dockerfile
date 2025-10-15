<<<<<<< HEAD
ARG PYTHON_VERSION=3.13-slim
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Dependências para psycopg2
=======
# Dockerfile para Fly.io - Django
ARG PYTHON_VERSION=3.13-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do psycopg2
>>>>>>> 94eb6fd2039fdadd0b769f037aff2dc07de085ab
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

<<<<<<< HEAD
=======
# Define diretório do projeto
>>>>>>> 94eb6fd2039fdadd0b769f037aff2dc07de085ab
WORKDIR /code

# Instala poetry
RUN pip install poetry

<<<<<<< HEAD
# Copia arquivos de dependências
COPY 7_django_framework/bookstore/pyproject.toml 7_django_framework/bookstore/poetry.lock /code/

RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction

# Copia todo o projeto Django
COPY 7_django_framework/bookstore/ /code/

# Coleta os static files
RUN python /code/manage.py collectstatic --noinput
=======
# Copia apenas arquivos de dependências primeiro
COPY pyproject.toml poetry.lock /code/

# Configura poetry para não criar virtualenv
RUN poetry config virtualenvs.create false

# Instala dependências do projeto
RUN poetry install --only main --no-root --no-interaction

# Copia todo o projeto Django
COPY . /code/
>>>>>>> 94eb6fd2039fdadd0b769f037aff2dc07de085ab

# Define SECRET_KEY de ambiente para produção
ENV SECRET_KEY "R0oHkQlrWpr8ihYsI5gIqz5n5pAwVE25JxqaEk2MRkGEfXjP0D"

<<<<<<< HEAD
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "bookstore.wsgi"]
=======
# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expõe porta
EXPOSE 8080

# Comando padrão para iniciar o Gunicorn
CMD ["gunicorn","--bind",":8080","--workers","2","bookstore.wsgi"]
>>>>>>> 94eb6fd2039fdadd0b769f037aff2dc07de085ab
