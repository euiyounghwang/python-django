
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


es_client = Elasticsearch(hosts=os.getenv("ES_HOST", "http://localhost:9209"),
                          headers=get_headers(),
                          verify_certs=False,
                          timeout=600
)

SearchOmniHandlerInject = SearchOmniHandler(es_client, logger)