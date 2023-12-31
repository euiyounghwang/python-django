#!/bin/bash
set -e

# Activate virtualenv && run serivce

# cd /Users/euiyoung.hwang/ES/Python_Workspace/python-django
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

cd $SCRIPTDIR
source .venv/bin/activate

./wait_for_es.sh http://localhost:9200

# poetry run python manage.py migrate 
# -- runserver is for dev env
# poetry run python manage.py runserver 9999

# -- NginX + Gunicorn for Prod
# https://wikidocs.net/6601
export DJANGO_SETTINGS_MODULE="config.settings_prod"
poetry run gunicorn -w 4 --bind 0:9999 config.wsgi:application

# Create project
# python manage.py startapp rest_api
