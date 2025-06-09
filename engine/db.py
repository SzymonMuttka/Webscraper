import os
from pymongo import MongoClient

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://21278:04291006312@mongodb21278.94q2jcy.mongodb.net/PRIR)')

def get_collection():
    client = MongoClient(MONGO_URI)
    db = client["PRIR"]
    return db["PRIR"]

def save_result(result):
    collection = get_collection()
    collection.insert_one(result)