# middleware.py
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwt_auth = JWTAuthentication()
        header = request.COOKIES.get('access_token')
        if header:
            raw_token = header
            validated_token = jwt_auth.get_validated_token(raw_token)
            request.user = jwt_auth.get_user(validated_token)
        return self.get_response(request)