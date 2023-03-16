import os


class Config:
    mongodb_uri: str
    mongodb_notifications_db: str
    mongodb_notifications_collection: str
    simulator_interval_seconds: int

    @staticmethod
    def default():
        mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
        mongodb_notifications_db = os.getenv('MONGODB_NOTIFICATIONS_DB', 'notifications')
        mongodb_notifications_collection = os.getenv('MONGODB_NOTIFICATIONS_COLLECTION', 'notifications')
        simulator_interval_seconds = int(os.getenv('SIMULATOR_INTERVAL_SECONDS', 3))
        c = Config()
        c.mongodb_uri = mongodb_uri
        c.mongodb_notifications_db = mongodb_notifications_db
        c.mongodb_notifications_collection = mongodb_notifications_collection
        c.simulator_interval_seconds = simulator_interval_seconds
        return c
