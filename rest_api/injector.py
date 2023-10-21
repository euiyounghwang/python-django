
from .config.log_config import create_log
# from config import config
# from service.Handler.search.SearchOmniHandler import (SearchOmniHandler)
from .service.Handler.SearchOmniHandler import SearchOmniHandler
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

import json
import os

load_dotenv()
logger = create_log()

def get_headers():
    ''' Elasticsearch Header '''
    return {'Content-type': 'application/json', 'Connection': 'close'}


from django.conf import settings

# --
# Get config from settings
# ES_HOST = os.getenv("ES_HOST", "http://localhost:9209")
ES_HOST = os.getenv("ES_HOST", getattr(settings, 'GLOBAL_ES_HOST'))

es_client = Elasticsearch(hosts=ES_HOST,
                          headers=get_headers(),
                          verify_certs=False,
                          timeout=600
)

SearchOmniHandlerInject = SearchOmniHandler(es_client, logger)