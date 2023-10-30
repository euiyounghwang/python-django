
from .config.log_config import create_log
# from config import config
# from service.Handler.search.SearchOmniHandler import (SearchOmniHandler)
from .service.Handler.SearchOmniHandler import (SearchOmniHandler)
from .service.Handler.QueryBuilder import QueryBuilder
from .service.Handler.redis_handler import Cache
from .service.Utils.ES_Utils import (get_headers)
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

import json
import os

load_dotenv()
logger = create_log()


from django.conf import settings

# --
# Get config from settings
# ES_HOST = os.getenv("ES_HOST", "http://localhost:9209")
# Docker -e argument
ES_HOST = os.getenv("ES_HOST", getattr(settings, 'GLOBAL_ES_HOST'))
URL_HOST = os.getenv("ES_HOST", getattr(settings, 'GLOBAL_HOST_URL'))

# --
# Redis
RedisHanlderInject = os.getenv("_HOST", getattr(settings, 'GLOBAL_ES_HOST'))

from django.core.cache import cache
Redis_Cache = Cache(logger, cache)
# --

es_client = Elasticsearch(hosts=ES_HOST,
                          headers=get_headers(),
                          verify_certs=False,
                          timeout=600
)

SearchOmniHandlerInject = SearchOmniHandler(es_client, logger)
QueryBuilderInject = QueryBuilder(es_client, logger)