from rest_framework.exceptions import ValidationError


class VehicleAlreadyExists(ValidationError):
    status_code = 409
    default_code = "VEHICLE_ALREADY_EXISTS"
    default_detail = "Vehicle exists that is not sold yet."
