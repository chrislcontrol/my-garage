from datetime import datetime
from decimal import Decimal
from logging import getLogger

from rest_framework.exceptions import ValidationError

from my_garage.clients.models import Client
from my_garage.handlers import handle_response_body
from my_garage.providers.fipe_provider import FipeProvider
from my_garage.providers.utils import convert_string_price_to_decimal
from my_garage.vehicles.exceptions.vehicle_already_exists import VehicleAlreadyExists
from my_garage.vehicles.models import Vehicle
from my_garage.vehicles.repositories import VehicleRepository
from utils.interfaces import UseCase

logger = getLogger("__name__")


class PurchaseVehicleUseCase(UseCase):
    def __init__(self):
        self._vehicle_repository = VehicleRepository()
        self._fipe_provider = FipeProvider()
        self._handle_response_body = handle_response_body

    def execute(self, *,
                type: Vehicle.Types,
                purchase_value: Decimal,
                purchase_datetime: datetime,
                code_brand: str,
                code_model: str,
                year: int,
                model_year_id: str,
                tag: str,
                km: int,
                has_extra_key: bool,
                has_owner_handbook: bool,
                gear: Vehicle.Gear,
                is_unique_old_owner: bool,
                last_owner_genre: Vehicle.LastOwnerGenre = None,
                has_vng: bool = False,
                engine_capacity: int,
                cylinders: int,
                client: Client) -> Vehicle:

        already_exists = self._vehicle_repository.already_exists(client=client, tag=tag)
        if already_exists:
            logger.info(f"Vehicle already exists for client={client.username}, tag={tag}.")
            raise VehicleAlreadyExists()

        fipe_info = self._get_remote_fipe_info(vehicle_type=type,
                                               brand_id=code_brand,
                                               model_id=code_model,
                                               year_id=model_year_id)
        if year < (fipe_info['modelYear'] - 1) or year > fipe_info['modelYear']:
            raise ValidationError(f"Year must be between {fipe_info['year'] - 1} and {fipe_info['year']}")

        fipe_value = convert_string_price_to_decimal(fipe_info['price'])

        return self._vehicle_repository.create(type=type,
                                               fipe_code=fipe_info['codeFipe'],
                                               purchase_value=purchase_value,
                                               purchase_datetime=purchase_datetime,
                                               fipe_value_on_create=fipe_value,
                                               brand=fipe_info['brand'],
                                               code_brand=code_brand,
                                               model=fipe_info['model'],
                                               code_model=code_model,
                                               year=year,
                                               model_year=fipe_info['modelYear'],
                                               model_year_id=model_year_id,
                                               fuel=fipe_info['fuel'],
                                               fuel_acronym=fipe_info['fuelAcronym'],
                                               km=km,
                                               tag=tag,
                                               has_extra_key=has_extra_key,
                                               has_owner_handbook=has_owner_handbook,
                                               gear=gear,
                                               is_unique_old_owner=is_unique_old_owner,
                                               last_owner_genre=last_owner_genre,
                                               has_vng=has_vng,
                                               engine_capacity=engine_capacity,
                                               cylinders=cylinders,
                                               client=client)

    def _get_remote_fipe_info(self, *,
                              vehicle_type: Vehicle.Types,
                              brand_id: str,
                              model_id: str,
                              year_id: str) -> dict:
        response = self._fipe_provider.get_fipe_info(vehicle_type=vehicle_type,
                                                     brand_id=brand_id,
                                                     year_id=year_id,
                                                     model_id=model_id)
        if not response.ok:
            raise ValidationError("Failed to get FIPE info.")

        return self._handle_response_body(response)
