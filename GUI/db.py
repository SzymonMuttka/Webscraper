import os
from pymongo import MongoClient

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://21278:04291006312@mongodb21278.94q2jcy.mongodb.net/PRIR)')

def get_all_results():
    client = MongoClient(MONGO_URI)
    db = client['PRIR']
    collection = db['PRIR']
    results = collection.find().sort("timestamp", -1)
    return [
        {
            "url": r.get("url", ""),
            "title": r.get("title", ""),
            "headers": r.get("headers", []),
            "links": r.get("links", []),
            "emails": r.get("emails", []),
        }
        for r in results
    ]
