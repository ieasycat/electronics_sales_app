#! /bin/bash

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata main_fixtures.json

python manage.py collectstatic --no-input

gunicorn electronics_sales.wsgi:application --bind 0.0.0.0:8000 --reload -w 4