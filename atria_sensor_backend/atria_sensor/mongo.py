from django.conf import settings
from pymongo import MongoClient, ASCENDING
import math

client = MongoClient(connect=False, host='mongo', username='atria', password='atria')


def insert_one_doc_to_mongo(db_name, collection_name, document):
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_one(document)


def insert_many_doc_to_mongo(db_name, collection_name, document_list):
    db = client[db_name]
    collection = db[collection_name]
    res = collection.insert_many(document_list, ordered=False)    
    return res


def get_docs_by_query(db_name, collection_name, query, doc_limit=None):
    db = client[db_name]
    collection = db[collection_name]
    if doc_limit != None:
        return list(collection.find(query).limit(doc_limit))
    else:
        return list(collection.find(query))        
 
