import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Notification


@sync_to_async
def get_notifications(user, new_notification=None):
    notifications = user.notification_to.all().order_by('-timestamp')
    if new_notification:
        notifications = list(notifications)
        notifications.append(new_notification)
    return [{'message': n.message, 'since': n.since} for n in notifications]


@sync_to_async
def create_notification(user, message):
    notification = Notification.objects.create(to=user, message=message)
    return notification


class NotificationWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        if user.is_authenticated:
            notifications = await get_notifications(user)
            await self.accept()
            await self.send(json.dumps({'notifications': notifications}))
            await self.channel_layer.group_add(f"notification_{self.scope['user'].id}",self.channel_name)
        else:
            await self.close()

    async def disconnect(self):
        pass

    async def user_notification(self, event):
        new_notification = await create_notification(self.scope['user'], event["message"])

        notifications = await get_notifications(self.scope['user'], new_notification=new_notification)
        await self.send(text_data=json.dumps({
            "notifications": notifications
        }))
