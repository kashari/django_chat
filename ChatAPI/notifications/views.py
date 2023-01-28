from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from users.models import User


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_notifications(request):
    """List all the user notifications."""
    headers = request.headers
    if 'Authorization' in headers:
        token_name, token_key = headers['Authorization'].split()
        if token_name == 'Bearer':
            token = AccessToken(token_key)
            user = User.objects.get(id=token.payload['user_id'])
            notifications = Notification.objects.filter(to=user).order_by('timestamp')
            serializer = NotificationSerializer(instance=notifications, many=True)
            return Response(serializer.data)
    return Response({'message': 'You need to be authenticated to get the data of this endpoint.'})
