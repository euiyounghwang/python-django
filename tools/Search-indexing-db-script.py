
# -*- coding: utf-8 -*-
import sys
import json

from elasticsearch import Elasticsearch
import argparse
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

MAX_BYTES = 1048576


class Databases():
    
    def __init__(self):
        self.db = psycopg2.connect(os.getenv("DATABASE_URL", "postgresql://postgres:1234@{}:{}/postgres".format("localhost", 15432)))
        self.cursor = self.db.cursor(cursor_factory=RealDictCursor)

    # def __del__(self):
    #     self.db.close()
    #     self.cursor.close()

    def datetime_handler(self, x):
        if isinstance(x, datetime):
                return x.strftime('%Y-%m-%d %H:%M:%S')
        raise TypeError("Unknown Type")

    def execute(self,query,args={}):
        # self.cursor.execute(query,args)
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        rows = [dict(row) for row in data]
        print(json.dumps(rows, indent=2, default=self.datetime_handler))
        return rows

    def commit(self):
        self.cursor.commit()
        
    def close(self):
        self.db.close()
        self.cursor.close()
        print("Closed successfully!!!") 


class Search():
    ''' elasticsearch class '''
    
    def __init__(self, host):
        self.timeout = 60
        self.es_client = Elasticsearch(hosts=host, headers=self.get_headers(), timeout=self.timeout)
    
    
    def get_headers(self):
        ''' Elasticsearch Header '''
        return {
            'Content-type': 'application/json', 
            'Connection': 'close'
        }
        
    
    def Get_Buffer_Length(self, docs):
        """
        :param docs:
        :return:
        """
        max_len = 0
        for doc in docs:
            max_len += len(str(doc))

        return max_len
    
        
    def create_index(self, _index):
        print(self.es_client)
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
            if self.es_client.indices.exists(index=_index):
                self.es_client.indices.delete(index=_index, ignore=[400, 404])
                print("Successfully deleted: {}".format(_index))

            print('Creating..')
            # now create a new index
            self.es_client.indices.create(index=_index, body=mapping)
            # es_client.indices.put_alias(index, "omnisearch_search")
            self.es_client.indices.refresh(index=_index)
            print("Successfully created: {}".format(_index))
            
        except Exception as error:
            print('Error: {}, index: {}'.format(error, _index))



def get_db_connection():
    ''' postgres connection '''
    try: 
        client = Databases()
        print("Connected successfully!!!") 
        return client
    except Exception as e:
        print("mongodb_connection - {}".format(str(e)))
        
        
if __name__ == "__main__":
    
    ''' 
        https://edudeveloper.tistory.com/131
        Run (Postgresql DB Select and Indexing into Elasticsearch, Scripts)
        poetry run python ./tools/Search-indexing-db-script.py --es=http://localhost:9209  --index=search_indexing-db 
        poetry run python ./search-indexing-script.py --es $ES_HOST --DATABASE_URL $DATABASE_URL --index $INDEX_NAME (Docker Based)
    '''
    parser = argparse.ArgumentParser(description="Index into Elasticsearch using this script")
    parser.add_argument('-e', '--es', dest='es', default="http://localhost:9209", help='host target')
    parser.add_argument('-i', '--index', dest='index', default="search_indexing-db", help='host target')
    args = parser.parse_args()
    
    if args.es:
        es_host = args.es
        
    if args.index:
        es_index_name = args.index
        
    es_client, client = None, None
    try:
        client = Databases()
        if client:
            print("Connected successfully!!!")
            
        ''' offset == size, limit == paging number '''
        client.execute(
                query='SELECT * from {} LIMIT 10 OFFSET 0'.format('public.student'),
                
        )
        
        # es_client = Search(host=es_host)
        # es_client.create_index(_index=es_index_name)
            
    except Exception as e:
        print("Connection - {}".format(str(e)))
        
    finally:
        client.close()