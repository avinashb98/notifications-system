import time
import uuid
from pydantic import BaseModel

from .enums import NotificationReadStatus, NotificationIdentifier


class NotificationWrite(BaseModel):
    title: str
    description: str | None
    receiver_user_id: str
    identifier: NotificationIdentifier | None


class Notification:
    notification_id: str
    title: str
    description: str | None
    receiver_user_id: str
    read_status: NotificationReadStatus
    identifier: NotificationIdentifier | None

    # timestamps
    created_at: int
    updated_at: int

    def __init__(self,
                 receiver_user_id: str, title: str,
                 notification_id: str = None,
                 created_at: int = None,
                 updated_at: int = None,
                 read_status: str = None,
                 description: str = None,
                 identifier: NotificationIdentifier = None):
        if notification_id is None:
            notification_id = str(uuid.uuid4())
        if read_status is None:
            read_status = NotificationReadStatus.UNREAD.value
        if created_at is None:
            created_at = int(time.time())
        if updated_at is None:
            updated_at = int(time.time())

        self.notification_id = notification_id
        self.title = title
        self.receiver_user_id = receiver_user_id
        self.description = description
        self.identifier = NotificationIdentifier(identifier)
        self.read_status = read_status

        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def new_from_input(notif_input: NotificationWrite):
        return Notification(notif_input.receiver_user_id, notif_input.title,
                            description=notif_input.description, identifier=notif_input.identifier)

    def to_dict(self):
        return {
            'notification_id': self.notification_id,
            'title': self.title,
            'description': self.description,
            'receiver_user_id': self.receiver_user_id,
            'identifier': self.identifier.value,
            'read_status': self.read_status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    @staticmethod
    def from_dict(dictionary: dict):
        return Notification(**dictionary)
