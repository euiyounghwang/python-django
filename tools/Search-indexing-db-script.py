
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
import pandas as pd

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
        # print(json.dumps(rows, indent=2, default=self.datetime_handler))
        return json.loads(json.dumps(rows, indent=2, default=self.datetime_handler))

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


    def buffered_json(self, df, _index):
        print("buffer_indexing_mode_run Loading..")
        print(df)
        actions = []
       
        # creating a list of dataframe columns 
        columns = list(df) 
        for row in list(df.values.tolist()):
            rows_dict = {}
            for i, colmun_name in enumerate(columns):
                rows_dict.update({colmun_name : row[i]})
            # print(rows_dict)
            actions.append({'index': {'_index': _index}})
            actions.append(rows_dict)
        print(json.dumps(actions, indent=2))


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
        total_size = 0
        paging_size = 10.0
        limit_position = 0
        client = Databases()
        es_client = Search(host=es_host)
        if client:
            print("Connected successfully!!!")
        
        ''' total count '''
        cnt_list = (client.execute(query='SELECT COUNT(*) as cnt from {}'.format('public.student'),))
        
        if cnt_list and isinstance(cnt_list, list):
            total_size = int(cnt_list[0]['cnt'])
            if total_size > 0:
                limit_position = int(total_size//paging_size)
            print('total cnt - {}, limit_position - {}'.format(total_size, limit_position))
            
        ''' offset == size, limit == paging number '''
        for running_query in range(0, limit_position+1):
            rows = client.execute(query='SELECT * from {} LIMIT {} OFFSET {}'.format(
                                    'public.student', 
                                    int(paging_size),
                                    int(running_query),))
            print(json.dumps(rows, indent=2))
            ''' 
            [
                {'index': {'_index': _metrics_index}
                {"id": 1, "name": "11", "grade": 2147483647, "age": 2147483647, "home_address": "string", "date": "2023-11-02 04:16:35", "gender": "Male"}
                {'index': {'_index': _metrics_index}
                ...
            ]
            Time Complexity : O(N^2) if it will make buffer_indexing_json with header like the above
            for row in rows:
                for k, v in row.items():
                    print({k : v})
            We can make the same way using Dataframe after convert df to json
            '''
            es_client.buffered_json(df=pd.DataFrame.from_dict(rows), _index=es_index_name)
        
        
        # es_client.create_index(_index=es_index_name)
                   
    except Exception as e:
        print("Connection - {}".format(str(e)))
        
    finally:
        client.close()