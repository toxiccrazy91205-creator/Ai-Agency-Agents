#!/bin/bash

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn ai_agency.wsgi:application --bind 0.0.0.0:$PORT
