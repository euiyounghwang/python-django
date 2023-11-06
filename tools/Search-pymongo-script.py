# -*- coding: utf-8 -*-
import sys
import datetime
from pymongo import MongoClient
import json


def mongodb_connection():
    ''' mongodb connection '''
    try: 
        conn = MongoClient("mongodb://postgres:1234@localhost:27017/") 
        print("Connected successfully!!!") 
        return conn
    except Exception as e:
        print("mongodb_connection - {}".format(str(e)))


def mongodb_insert(client):
    ''' delete collection and insert '''
    try:
        # Getting the database instance
        db = client['local']

        # Creating a collection
        coll = db['example']
        
        res = db['example'].drop()
        
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
        
        res = coll.insert_many(data)
        print("Data inserted ......")
        print(res.inserted_ids)

    except Exception as e:
        print(str(e))
        
        
def mongodb_select(client):
    try:
        #Getting the database instance
        db = client['local']

        #Creating a collection
        coll = db['example']

        cursor = coll.find({})
        for document in cursor:
            print(json.dumps(document, indent=2))

    except Exception as e:
        print(str(e))
     
     
if __name__ == "__main__":
   
    try:
        client = mongodb_connection()
        mongodb_insert(client)
        mongodb_select(client)
    finally:
        client.close()
