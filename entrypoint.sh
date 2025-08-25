#!/bin/bash
set -e

# Run migrations
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Create superuser if not exists (env vars required)
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
  python manage.py createsuperuser \
    --noinput \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    || true
fi

# Start server
exec python manage.py runserver 0.0.0.0:8000
