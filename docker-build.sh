#!/bin/bash

set -eu

#docker build --no-cache \

docker build \
  -f "$(dirname "$0")/Dockerfile" \
  -t fn-django-search-api:test \
  --target test \
  "$(dirname "$0")/."


docker build \
  -f "$(dirname "$0")/Dockerfile" \
  -t fn-django-search-api:es \
  --target runtime \
  "$(dirname "$0")/."

