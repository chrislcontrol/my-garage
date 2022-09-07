from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from my_garage.api_errors_mixin import ApiErrorsMixin
from my_garage.authentication.app_authentication import AppAuthentication


class BaseAPIView(ApiErrorsMixin, APIView):
    authentication_classes = [AppAuthentication]
    permission_classes = [IsAuthenticated]
    success_status = {"POST": status.HTTP_201_CREATED,
                      "GET": status.HTTP_200_OK,
                      "PUT": status.HTTP_202_ACCEPTED,
                      "PATCH": status.HTTP_202_ACCEPTED,
                      "DELETE": status.HTTP_202_ACCEPTED}
    serializer_classes = {}
    output_serializers = {}

    def __get_serializer(self, serializer_dict: dict, method):
        serializers = {key.lower(): value for key, value in serializer_dict.items()}
        return serializers.get(method.lower())

    def serializer(self, *args, **kwargs):
        return self.__get_serializer(serializer_dict=self.serializer_classes,
                                     method=self.request.method)(*args, **kwargs)

    def output_serializer(self, *args, **kwargs):
        return self.__get_serializer(serializer_dict=self.output_serializers,
                                     method=self.request.method)(*args, **kwargs)

    @property
    def status_ok(self) -> int:
        return self.success_status.get(self.request.method.upper(), status.HTTP_200_OK)
