from rest_framework.exceptions import AuthenticationFailed
import jwt
from functools import wraps
def only_authorized(function):
    @wraps(function)
    def wrap(request,*args,**kwargs):
        token=request.headers['Authorization']
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        return function(request,*args,**kwargs)
    return wrap