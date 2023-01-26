from channels.db import database_sync_to_async
from rest_framework_simplejwt.tokens import AccessToken
from channels.middleware import BaseMiddleware
from users.models import User


@database_sync_to_async
def get_user(token_key):
    token = AccessToken(token_key)
    user = User.objects.get(id=token.payload['user_id'])
    return user


class TokenAuthMiddleware(BaseMiddleware):

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        headers = dict(scope['headers'])
        if b'authorization' in headers:
            token_name, token_key = headers[b'authorization'].decode().split()
            if token_name == 'Bearer':
                scope['user'] = await get_user(token_key)
        return await super().__call__(scope, receive, send)
