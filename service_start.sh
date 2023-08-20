#!/bin/bash
set -e

# Activate virtualenv && run serivce

cd /Users/euiyoung.hwang/ES/Python_Workspace/python-django
source .venv/bin/activate

# poetry run python manage.py migrate 
poetry run python manage.py runserver 5001