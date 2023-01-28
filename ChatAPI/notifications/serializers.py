from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    to = UserSerializer()
    since = serializers.ReadOnlyField()

    class Meta:
        model = Notification
        fields = ['to', 'message', 'opened', 'since']