#!/bin/bash
set -e

echo "Waiting for PostgreSQL..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done

echo "Applying Django migrations..."
poetry run python manage.py migrate --noinput

echo "Collecting static files..."
poetry run python manage.py collectstatic --noinput

echo "Starting Gunicorn server..."
poetry run gunicorn config.wsgi:application --bind 0.0.0.0:8001 --workers 4 --threads 4
