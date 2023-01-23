from django.urls import path
from .views import *

app_name = 'chat'

urlpatterns = [
    path('start/', start_convo, name='start_convo'),
    path('<int:convo_id>/', get_conversation, name='get_conversation'),
    path('', conversations, name='conversations')
]
