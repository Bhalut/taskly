# syntax=docker/dockerfile:1

# --- BUILD STAGE ---
FROM python:3.11-slim AS builder

WORKDIR /app
        
RUN apt-get update && apt-get install -y gcc libpq-dev netcat-openbsd

RUN pip install poetry
        
COPY pyproject.toml poetry.lock ./
        
RUN poetry config virtualenvs.create false && poetry lock && poetry install --only main --no-root
        
COPY . .
        
# --- FINAL STAGE ---
FROM python:3.11-slim
        
WORKDIR /app
        
RUN apt-get update && apt-get install -y libpq-dev netcat-openbsd && rm -rf /var/lib/apt/lists/*
        
RUN pip install poetry
        
COPY --from=builder /app /app
        
RUN chmod +x /app/entrypoint.sh

RUN poetry config virtualenvs.create false && poetry lock && poetry install --only main --no-root

ENV PYTHONUNBUFFERED=1
        
CMD ["/app/entrypoint.sh"]
