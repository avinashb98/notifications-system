from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        print(f'user {user_id} connected')
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: str, websocket: WebSocket):
        print(f'user {user_id} disconnected')
        del self.active_connections[user_id]

    def get_user_connection(self, user_id: str) -> WebSocket | None:
        if self.active_connections.get(user_id) is None:
            return None
        return self.active_connections.get(user_id)

    async def send_message(self, user_id: str, message: str):
        conn = self.get_user_connection(user_id)
        if conn is None:
            return
        await conn.send_text(message)


manager = ConnectionManager()
