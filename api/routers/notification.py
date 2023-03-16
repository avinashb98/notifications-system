from fastapi import APIRouter, Depends, BackgroundTasks
from services.notification import NotificationServiceV1
from entities import NotificationWrite
from services.notification.base import NotificationService

from services import NotifierService, global_connection_manager

router = APIRouter(
    prefix="/notification",
    tags=['Notifications']
)


def get_service() -> NotificationService:
    svc_v1 = NotificationServiceV1()
    return svc_v1


@router.post("/", status_code=201)
async def create_notification(notification: NotificationWrite, background_tasks: BackgroundTasks,
                              svc: NotificationService = Depends(get_service)):
    created_notif = svc.create_notif(notification)
    notifier = NotifierService(notification.receiver_user_id, global_connection_manager)
    background_tasks.add_task(notifier.send_notification, created_notif)
    return {
        "message": "new notification created",
        "data": created_notif.to_dict()
    }


@router.get("/{receiver_user_id}")
def read_notifications(receiver_user_id: str, skip: int = 0, limit: int = 10,
                       svc: NotificationService = Depends(get_service)):
    notifications = svc.get_notifications(receiver_user_id, skip, limit)
    return {
        "message": "list of notifications",
        "data": [n.to_dict() for n in notifications]
    }


@router.patch("/read")
def mark_notification_read(notification_id: str, svc: NotificationService = Depends(get_service)):
    success = svc.mark_notification_read(notification_id)
    return {"success": success}
