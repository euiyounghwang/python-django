
# -*- coding: utf-8 -*-
import sys
import json

from elasticsearch import Elasticsearch
import argparse
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

MAX_BYTES = 1048576


class Databases():
    
    def __init__(self):
        self.db = psycopg2.connect(os.getenv("DATABASE_URL", "postgresql://postgres:1234@{}:{}/postgres".format("localhost", 15432)))
        self.cursor = self.db.cursor()

    # def __del__(self):
    #     self.db.close()
    #     self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()
        
    def close(self):
        self.db.close()
        self.cursor.close()
        print("Closed successfully!!!") 


def get_db_connection():
    ''' postgres connection '''
    try: 
        client = Databases()
        print("Connected successfully!!!") 
        return client
    except Exception as e:
        print("mongodb_connection - {}".format(str(e)))
        
def get_headers():
    ''' Elasticsearch Header '''
    return {'Content-type': 'application/json', 'Connection': 'close'}


def get_es_instance(_host):
    # create a new instance of the Elasticsearch client class
    es_client = Elasticsearch(hosts=_host, headers=get_headers(), timeout=5)
    return es_client

def create_index(es_client, _index):
    print(es_client)
    mapping = {
        "mappings": {
            "properties": {
                "title": {
                    "type": "text",
                    "analyzer": "standard",
                    "fields": {
                        "keyword": {
                            "type": "keyword"
                        }
                    }
                }
            }
        }
    }

    try:
        if es_client.indices.exists(index=_index):
            es_client.indices.delete(index=_index, ignore=[400, 404])
            print("Successfully deleted: {}".format(_index))

        print('Creating..')
        # now create a new index
        es_client.indices.create(index=_index, body=mapping)
        # es_client.indices.put_alias(index, "omnisearch_search")
        es_client.indices.refresh(index=index)
        print("Successfully created: {}".format(_index))
    except Exception as error:
        print('Error: {}, index: {}'.format(error, _index))


def Get_Buffer_Length(docs):
    """
    :param docs:
    :return:
    """
    max_len = 0
    for doc in docs:
        max_len += len(str(doc))

    return max_len



if __name__ == "__main__":
    try:
        client = get_db_connection()
    finally:
        client.close()