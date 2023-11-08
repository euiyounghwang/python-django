
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
from Search_Engine import Search

load_dotenv()


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


        
if __name__ == "__main__":
    
    ''' 
        https://edudeveloper.tistory.com/131
        Run (Postgresql DB Select and Indexing into Elasticsearch, Scripts)
        poetry run python ./tools/Search-indexing-db-script.py --es=http://localhost:9209  --index=search_indexing-db 
        poetry run python ./Search-indexing-db-script.py --es $ES_HOST --DATABASE_URL $DATABASE_URL --index $INDEX_NAME (Docker Based)
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
        paging_size = 10
        limit_position = 0
        
        client = Databases()
        if client:
            print("Connected successfully!!!")
        
        es_client = Search(host=es_host)
        es_client.create_index(_index=es_index_name)
        
        ''' total count '''
        cnt_list = (client.execute(query='SELECT COUNT(*) as cnt from {}'.format('public.student'),))
        
        if cnt_list and isinstance(cnt_list, list):
            total_size = int(cnt_list[0]['cnt'])
            if total_size > 0:
                limit_position = int(round((total_size//paging_size)+0.6))
            # print('total cnt - {}, limit_position - {}'.format(total_size, limit_position))
            
        ''' offset == size, limit == paging number '''
        for running_query in range(0, limit_position):
            print('Read DB : Retry [{}]'.format(running_query+1))
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
            es_client.buffered_json_to_es(df=pd.DataFrame.from_dict(rows), _index=es_index_name)
                   
    except Exception as e:
        print("Connection - {}".format(str(e)))
        
    finally:
        ''' Check if indesing process works fine '''
        es_client.post_search(_index=es_index_name)
        
        client.close()
        es_client.close()