from django.contrib.auth import authenticate
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def create_user(self, request):
    """Create a new user for this app, then user is eligible for authentication."""
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    user.set_password(user.password)
    user.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_users():
    """List all the app users."""
    users = User.objects.all().order_by('username')
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    """Authenticate the user by giving it a pair of tokens: refresh and access."""
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        token = RefreshToken.for_user(user)
        return Response({"access": str(token.access_token), "refresh": str(token)}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def logout(request):
    """Blacklist the refresh token: extract token from the header
      during logout request user and refresh token is provided."""
    old_token = request.data["refresh"]
    token = RefreshToken(old_token)
    token.blacklist()
    return Response("Successful Logout", status=status.HTTP_200_OK)
