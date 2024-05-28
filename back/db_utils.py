from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://admin:nxUOmifPzO5oDMsJ@cluster.uxhzlu5.mongodb.net/"
dbclient = MongoClient(uri)

def get_dbclient():
    return dbclient  # Function to access the client

def get_cluster():
    return dbclient["Cluster"]

def get_users_database():
    return get_cluster()["users"]