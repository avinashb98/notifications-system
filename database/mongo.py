from pymongo import MongoClient
from config import Config


def get_notifications_client(config: Config):
    connection_string = config.mongodb_uri
    client = MongoClient(connection_string)
    return client[config.mongodb_notifications_db]
