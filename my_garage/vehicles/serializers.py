from rest_framework import serializers

from my_garage.vehicles.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        exclude = ["client", "modified"]
        read_only_fields = [
            "id",
            "fipe_value_on_create",
            "fipe_code",
            "brand",
            "model",
            "model_year",
            "fuel",
            "fuel_acronym",
            "is_sold"
        ]
