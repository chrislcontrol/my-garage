from my_garage.clients.models import Client
from my_garage.vehicles.models import Vehicle


class VehicleRepository:
    def __init__(self):
        self.model = Vehicle

    def create(self, **fields) -> Vehicle:
        return self.model.objects.create(**fields)

    def already_exists(self, *, client: Client, tag: str) -> bool:
        return self.model.objects.filter(client=client, tag=tag, is_sold=False).exists()

