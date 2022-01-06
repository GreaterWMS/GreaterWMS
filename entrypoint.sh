#!/bin/bash

python manage.py makemigrations
python manage.py migrate
daphne -p 8008 greaterwms.asgi:application
