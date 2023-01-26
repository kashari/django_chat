from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

app_name = 'users'

urlpatterns = [
    path('api/register', create_user, name='create_user'),
    path('api/update_profile', update_profile, name='update_profile'),
    path('api/users', list_users, name='list_users'),
    path('api/users/bulk_create', bulk_create, name='bulk_create_users'),
    path('', login, name='login'),
    path('token/refresh', TokenRefreshView.as_view())
]
