#!/usr/bin/env bash
# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create admin user (optional; interactive setup is better)
python manage.py createsuperuser --username admin --password admin