import jwt
from django.conf import settings
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from .models import User

class JWTAuthentication(BasicAuthentication):

    def authenticate(self, request): #the name of this function must be authenticate beacuse we are using a specific framework
        header = request.headers.get('Authorization')

        if not header:
            return None # this request is not authenticated.

        if not header.startswith('Bearer'):
            raise PermissionDenied({'message': 'Invalid Authorization header'}) #send a 401 response

        token = header.replace('Bearer ', '') #get the token from the header

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=payload.get('sub'))
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied({'message': 'Invalid token'})
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid subject'})

        # 'authenticate' should return a tuple if auth is successful
        # the first element is the user, the second is the token (if used)
        # request.user will be the user
        # request.token will be the token
        return (user, token)
