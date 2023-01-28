from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'bio')
        extra_kwargs = {'password': {'write_only': True}}

        def update(self, instance, validated_data):
            instance.username = validated_data['username']
            instance.email = validated_data['email']
            instance.bio = validated_data['bio']
            instance.save(update_fields=['username', 'email', 'bio'])
            return instance
