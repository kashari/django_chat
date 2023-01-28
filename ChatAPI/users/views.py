import csv
from django.contrib.auth import authenticate
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def create_user(request):
    """Create a new user for this app, then user is eligible for authentication."""
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    user.set_password(user.password)
    user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_users(request):
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


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_profile(request):
    headers = request.headers
    if 'Authorization' in headers:
        token_name, token_key = headers['Authorization'].split()
        if token_name == 'Bearer':
            token = AccessToken(token_key)
            user = User.objects.get(id=token.payload['user_id'])
            serializer = UserSerializer(instance=user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.update(user, request.data)
            return Response({'message': f'User {user.username} updated successfully.'})
        return Response({'message': 'Something went wrong.'})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def bulk_create(request):
    file = request.FILES['file']
    if not file:
        return Response({'error': 'No file provided, or file not valid.'}, status=400)
    file_data = file.read().decode('utf-8')
    lines = file_data.split('\n')
    reader = csv.DictReader(lines)
    data = [User(**row) for row in reader]
    User.objects.bulk_create(data)
    return Response({'message': 'Users created successfully.'}, status=201)
