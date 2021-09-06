#!/bin/bash
python3 manage.py makemigrations
python3 manage.py migrate
daphne -p 8008 greaterwms.asgi:application