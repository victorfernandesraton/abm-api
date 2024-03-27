#!/bin/sh
source venv/bin/activate
gunicorn -b :8080 --access-logfile - --error-logfile - app.wsgi
