from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from my_garage.authentication.serializers import CustomAuthTokenSerializer
from utils.base_views import BaseAPIView


class AuthView(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    class OutputSerializer(serializers.Serializer):
        token = serializers.CharField()

    @swagger_auto_schema(
        responses={400: 'Bad request', 200: OutputSerializer},
        request_body=AuthTokenSerializer
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, args, kwargs)


class AuthLogoutView(BaseAPIView):
    get_response_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={'message': openapi.Schema(type=openapi.TYPE_STRING)})

    @swagger_auto_schema(responses={
        500: get_response_schema,
        204: get_response_schema
    })
    def get(self, request):
        try:
            request.user.auth_token.delete()
            return HttpResponse(b'{"message": "Logout successeful"}',
                                content_type='application/json',
                                status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return HttpResponse(b'{"message": "Problems for logout"}',
                                content_type='application/json',
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
