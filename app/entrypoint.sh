#!/bin/sh
python manage.py flush --no-input
python manage.py migrate
python manage.py add_categories
python manage.py add_owners
python manage.py add_equipment
python manage.py createsuperuser --username king --email no-reply@mail.com --no-input
python manage.py collectstatic --no-input

exec "$@"