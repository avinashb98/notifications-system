from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from api import notification_router
from services import global_connection_manager, NotifierService
from services.notification import NotificationServiceV1
from fastapi_utils.tasks import repeat_every
from config import Config
from simulator.seed import get_random_notification

default_config = Config.default()

app = FastAPI()

app.include_router(notification_router)


@app.websocket("/ws/v1/notifications/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await global_connection_manager.connect(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await global_connection_manager.send_message(user_id, f"{data}")
    except WebSocketDisconnect:
        global_connection_manager.disconnect(user_id, websocket)


svc_v1 = NotificationServiceV1()


# this periodic task simulates events that generate
# notifications and notifies the respective user with
# randomly generated notifications
@app.on_event("startup")
@repeat_every(seconds=default_config.simulator_interval_seconds)
async def remove_expired_tokens_task() -> None:
    new_notif = get_random_notification()
    created_notif = svc_v1.create_notif(new_notif)
    notifier = NotifierService(created_notif.receiver_user_id, global_connection_manager)
    await notifier.send_notification(created_notif)
