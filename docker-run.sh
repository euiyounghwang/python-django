#!/bin/bash

set -eu

SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

docker run --rm --platform linux/amd64 -it -d \
  --name fn-django-search-api --publish 9991:9999 --expose 9999 \
  --network bridge \
  -e DATABASE_URL=postgresql://postgres:1234@host.docker.internal:15432/postgres \
  -e ES_HOST=http://host.docker.internal:9203 \
  -e HOST=host.docker.internal \
  -e RABBIT_HOST=host.docker.internal \
  -e PUBLISH_QUEUE=fastapi_publish_queue \
  -e REDIS_HOST=host.docker.internal \
  -e REDIS_PORT=6379 \
  -e REDIS_DATABASE=0 \
  -v "$SCRIPTDIR:/app/FN-Django-Services/" \
  fn-django-search-api:es


