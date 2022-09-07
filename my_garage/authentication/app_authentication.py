from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class AppAuthentication(TokenAuthentication):
    def authenticate(self, request):
        try:
            credentials = super().authenticate(request)
            if not credentials:
                return None

            return credentials
        except AuthenticationFailed:
            return None
