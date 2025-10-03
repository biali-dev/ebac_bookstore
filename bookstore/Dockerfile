# Base Python
FROM python:3.11-slim

# Evita criação de arquivos .pyc e habilita buffer de saída
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.8.3 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/tmp/poetry_cache'

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev \
        gcc \
    && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Instala psycopg2
RUN pip install psycopg2

# Copia arquivos de dependências
COPY pyproject.toml poetry.lock* ./

# Instala dependências sem pacotes de dev
RUN poetry install --no-root --only main

# Copia o restante do código
COPY . .

EXPOSE 8000

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
