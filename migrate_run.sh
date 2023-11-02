#!/bin/bash
set -e

# Activate virtualenv && run serivce

# cd /Users/euiyoung.hwang/ES/Python_Workspace/python-django
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

cd $SCRIPTDIR
source .venv/bin/activate

python manage.py showmigrations rest_api --settings=config.settings_dev
# -- Record & detect about the changing for the model
python manage.py makemigrations rest_api --settings=config.settings_dev
# -- Update to DB if any changes in the model (this step requires in the Django)
python manage.py migrate rest_api --settings=config.settings_dev