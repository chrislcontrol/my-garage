from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from my_garage.clients.models import Client
from my_garage.clients.serializers import ClientSerializer
from utils.base_views import BaseAPIView


class ClientsView(BaseAPIView):
    serializer_class = ClientSerializer
    success_status = {"POST": HTTP_200_OK}

    @swagger_auto_schema(request_body=serializer_class, responses={success_status["POST"]: serializer_class()})
    @transaction.atomic
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        client = Client(username=serializer.validated_data['username'], name=serializer.validated_data['name'])
        client.set_password(serializer.validated_data['password'])
        client.save()
        Token.objects.create(user=client)
        return Response(self.serializer_class(instance=client).data)
