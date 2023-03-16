from pymongo.database import Database
from pymongo.cursor import Cursor
from config import Config

from entities import NotificationReadStatus
from .base import NotificationRepository
from entities.notification import NotificationWrite, Notification


class MongoRepository(NotificationRepository):
    def __init__(self, db: Database, config: Config):
        self.collection = db[config.mongodb_notifications_collection]

    def create_notif(self, notification_input: NotificationWrite) -> Notification:
        notification = Notification.new_from_input(notification_input)
        document = notification.to_dict()
        self.collection.insert_one(document)
        return notification

    def mark_notification_read(self, notification_id: str) -> bool:
        result = self.collection.find_one_and_update(
            {'notification_id': notification_id},
            {'$set': {'read_status': NotificationReadStatus.READ.value}}
        )
        return result is not None

    def get_notifications(self, receiver_user_id: str, page: int = 0, limit: int = 10) -> list[Notification]:
        cursor = self.collection.find({'receiver_user_id': receiver_user_id})\
            .sort('created_at', -1)\
            .skip(page*limit)\
            .limit(limit)
        return self.__map_documents_to_notifications(cursor)

    @staticmethod
    def __map_documents_to_notifications(cursor: Cursor) -> list[Notification]:
        notifications: list[Notification] = []
        for document in cursor:
            del document['_id']
            notifications.append(Notification.from_dict(document))
        return notifications
