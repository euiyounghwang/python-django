#!/bin/bash
set -e

# Activate virtualenv && run serivce

# cd /Users/euiyoung.hwang/ES/Python_Workspace/python-django
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

cd $SCRIPTDIR
source .venv/bin/activate

# poetry run pytest -v rest_api/tests --junitxml=test-reports/junit/pytest.xml --cov-report html --cov
# poetry run pytest -v rest_api/tests --cov-report term-missing --cov html
# poetry run pytest -v rest_api/tests --cov-report term-missing --cov
poetry run pytest -v rest_api/tests
# pytest -v rest_api/tests