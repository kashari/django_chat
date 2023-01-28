from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(
            f"notification_{self.scope['user'].id}",
            self.channel_name
        )

    async def disconnect(self):
        await self.channel_layer.group_discard(
            f"notification_{self.scope['user'].id}",
            self.channel_name
        )

    async def user_notification(self, event):
        await self.send(text_data=event["message"])
