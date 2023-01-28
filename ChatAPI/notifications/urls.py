from django.urls import path

from .views import *

app_name = 'notifications'

urlpatterns = [
    path('list_notifications', list_notifications, name='list_notifications'),
]
