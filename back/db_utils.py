from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

uri = os.getenv("MONGODB")
dbclient = MongoClient(uri)

def get_dbclient():
    return dbclient  # Function to access the client

def get_cluster():
    return dbclient["Cluster"]

def get_users_database():
    return get_cluster()["users"]

def get_news_database():
    return get_cluster()["news"]

def get_bots_database():
    return get_cluster()["bots"]