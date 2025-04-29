from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User, AnonymousUser
import jwt
from django.conf import settings


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        try:
            token = auth_header.split(' ')[1]

            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=['HS256']
            )

            user_id = payload.get('user_id')
            username = payload.get('username', f'user_{user_id}')

            user = User(id=user_id, username=username)
            user.is_active = True

            return (user, token)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired")
        except (jwt.DecodeError, jwt.InvalidTokenError):
            raise AuthenticationFailed("Invalid token")
        except Exception as e:
            raise AuthenticationFailed(f"Authentication failed: {e}")
