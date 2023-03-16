from config import Config
from entities import Notification, NotificationWrite
from repositories.notification import NotificationRepository
from database import get_notifications_client
from repositories.notification import MongoRepository
from .base import NotificationService


class NotificationServiceV1(NotificationService):
    repository: NotificationRepository

    def __init__(self, repository: NotificationRepository = None, config: Config = None):
        if config is None:
            config = Config.default()
        if repository is None:
            notifications_database_client = get_notifications_client(config)
            notif_repo = MongoRepository(notifications_database_client, config)
            self.repository = notif_repo

    def create_notif(self, notification_input: NotificationWrite) -> Notification:
        return self.repository.create_notif(notification_input)

    def mark_notification_read(self, notification_id: str) -> bool:
        return self.repository.mark_notification_read(notification_id)

    def get_notifications(self, user_id: str, page: int = 0, limit: int = 10) -> list[Notification]:
        return self.repository.get_notifications(user_id, page, limit)
