from abc import ABC, abstractmethod
from entities import NotificationWrite, Notification


class NotificationService(ABC):
    @abstractmethod
    def create_notif(self, notification_input: NotificationWrite) -> Notification:
        raise NotImplemented

    @abstractmethod
    def mark_notification_read(self, notification_id: str):
        raise NotImplemented

    @abstractmethod
    def get_notifications(self, user_id: str, page: int = 0, limit: int = 10) -> list[Notification]:
        raise NotImplemented
