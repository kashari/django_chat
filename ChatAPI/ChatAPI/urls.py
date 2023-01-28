from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('chat/', include('chat.urls', namespace='chat')),
]
