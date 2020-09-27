from pymongo import MongoClient
from config import Settings


def get_collection():
    cluster = MongoClient(Settings().connection_string)
    db = cluster[Settings().cluster_name]
    collection = db[Settings().collection_name]
    return collection


