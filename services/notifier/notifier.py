from fastapi import WebSocket

from services import ConnectionManager
from entities import Notification


class NotifierService:
    receiver_user_id: str
    websocket: WebSocket | None

    def __init__(self, receiver_user_id: str, conn_manager: ConnectionManager):
        self.receiver_user_id = receiver_user_id
        self.websocket = conn_manager.get_user_connection(receiver_user_id)

    async def send_notification(self, notification: Notification):
        if self.websocket is None:
            return
        await self.websocket.send_json({
            "type": "notification",
            "data": notification.to_dict()
        })
        print(f'triggered notification for user {self.receiver_user_id}', notification.to_dict())
