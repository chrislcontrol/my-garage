from django.urls import path

from my_garage.vehicles.views import PurshaceVehicleView

VEHICLES_PATH = "vehicles"
app_name = VEHICLES_PATH

urlpatterns = [
    path(f"{VEHICLES_PATH}/purchase", PurshaceVehicleView.as_view(), name=f"{VEHICLES_PATH}-create")
]
