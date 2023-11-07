# -*- coding: utf-8 -*-
import sys
import datetime
from pymongo import MongoClient
import json
import argparse
from Search_Engine import Search


class Databases():
    
    def __init__(self):
        self.client = MongoClient("mongodb://postgres:1234@localhost:27017/")
    
    
    def Select(self, db, collection):
        try:
            #Getting the database instance
            db = self.client[db]

            #Creating a collection
            coll = db[collection]

            cursor = coll.find({})
            for document in cursor:
                print(json.dumps(document, indent=2))

        except Exception as e:
            print(str(e))
     
     
    def Insert(self, db, collection, data):
        ''' delete collection and insert '''
        try:
            # Getting the database instance
            db = self.client[db]

            # Creating a collection
            coll = db[collection]
            
            res = db[collection].drop()
            
            res = coll.insert_many(data)
            print("Data inserted ......")
            print(res.inserted_ids)

        except Exception as e:
            print(str(e))
            
        
    def close(self):
        self.client.close()
        print("Closed successfully!!!") 


def get_db_connection():
    ''' postgres connection '''
    try: 
        client = Databases()
        print("Connected successfully!!!") 
        return client
    except Exception as e:
        print("get_db_connection - {}".format(str(e)))
        
       

     
if __name__ == "__main__":
    
    ''' 
        Run (Mongo DB Select and Indexing into Elasticsearch, Scripts)
        poetry run python ./tools/Search-pymongo-db-script.py --es=http://localhost:9209  --index=search_indexing-db 
        poetry run python ./search-pymongo-db-script.py --es $ES_HOST --DATABASE_URL $DATABASE_URL --index $INDEX_NAME (Docker Based)
    '''
    parser = argparse.ArgumentParser(description="Index into Elasticsearch using this script")
    parser.add_argument('-e', '--es', dest='es', default="http://localhost:9209", help='host target')
    parser.add_argument('-i', '--index', dest='index', default="search_indexing-db", help='host target')
    args = parser.parse_args()
    
    if args.es:
        es_host = args.es
        
    if args.index:
        es_index_name = args.index
        
    try:
         # Inserting document into a collection
        '''
            doc1 = {"name": "Ram", "age": "26", "city": "Hyderabad"}
            coll.insert_one(doc1)
            print(coll.find_one())
        '''
        data = [
            {"_id": "101", "name": "Ram", "age": "26", "city": "Hyderabad"},
            {"_id": "102", "name": "Rahim", "age": "27", "city": "Bangalore", "addr" : "addr"},
            {"_id": "103", "name": "Robert", "age": "28", "city": "Mumbai"}
        ]
                        
        client = get_db_connection()
        client.Insert(db='local', collection='example', data=data)
        client.Select(db='local', collection='example')
    finally:
        client.close()
