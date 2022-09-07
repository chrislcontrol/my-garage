from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from my_garage.vehicles.serializers import VehicleSerializer
from my_garage.vehicles.use_cases.purchase_vehicle_use_case import PurchaseVehicleUseCase
from utils.base_views import BaseAPIView


class PurshaceVehicleView(BaseAPIView):
    serializer_classes = {"POST": VehicleSerializer}
    success_status = {"POST": HTTP_201_CREATED}

    def __init__(self):
        super().__init__()
        self.purchase_vehicle_use_case = PurchaseVehicleUseCase()

    @swagger_auto_schema(request_body=serializer_classes['POST'],
                         responses={success_status["POST"]: serializer_classes['POST']()})
    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(True)

        vehicle = self.purchase_vehicle_use_case.execute(client=request.user, **serializer.validated_data)

        output = self.serializer(vehicle)

        return Response(data=output.data, status=self.status_ok)
