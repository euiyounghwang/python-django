#!/bin/bash
set -e

# sleep 60 
# --
# Conda
# --
# source /app/conda/bin/activate fn_fta_services
# cd /app/FN-FTA-Services

# --
# Poetry
# --
source /app/poetry-venv/bin/activate
cd /app/FN-Django-Services
# python -m py.test -v tests --disable-warnings
# py.test -v tests --disable-warnings
poetry run pytest -v rest_api/tests