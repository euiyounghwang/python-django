#!/bin/bash
set -e

source .venv/bin/activate

# Start to index with sample documents from .csv into the target ES instance
poetry run python ./tools/Search-indexing-script.py
