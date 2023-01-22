from django.urls import path
from .views import UserViewSet, AuthenticationViewSet

app_name = 'users'

urlpatterns = [
    path('api/register', UserViewSet),
    path('', AuthenticationViewSet)
]
