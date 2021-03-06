#!/bin/bash

dockerize -wait tcp://$1:$2 -timeout 60s

echo "database connected"

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata api/migrations/*.json

python manage.py runserver 0.0.0.0:8000