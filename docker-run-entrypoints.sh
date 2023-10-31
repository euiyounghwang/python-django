#!/bin/bash
set -ex

# sleep 60

# --
# Poetry v.
# --
source /app/poetry-venv/bin/activate
cd /app/FN-Django-Services
# poetry run python ./search-indexing-script.py --es $ES_HOST
# poetry run uvicorn main:app --reload --port=7000 --workers 4
# poetry run python manage.py runserver 9999
poetry run gunicorn -w 2 --bind 0:9999 config.wsgi:application

# --
# Conda v.
# --
# source /app/conda/bin/activate fn_fta_services
# cd /app/FN-FTA-Services
# exec uvicorn main:app --host=0.0.0.0 --port=7000 --workers 4