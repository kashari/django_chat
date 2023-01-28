from django.urls import re_path

from .consumers import *
from notifications.consumers import NotificationWebsocketConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
    re_path(r'ws/notifications/(?P<username>\w+)/$', NotificationWebsocketConsumer.as_asgi()),
]
