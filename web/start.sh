#!/bin/bash

python manage.py migrate
python manage.py createsuperuser --noinput --username=admin --email=test@mail.ru
python manage.py initial_data
exec python manage.py runserver 0.0.0.0:8000

