#!/bin/bash

if [ -f "/app/main.py" ]; then
    uvicorn main:app --host 0.0.0.0 --port 8000
elif [ -f "/app/manage.py" ]; then
    python manage.py runserver 0.0.0.0:8000
elif [ -f "/app/app.py" ]; then
    flask run --host 0.0.0.0 --port 8000
fi