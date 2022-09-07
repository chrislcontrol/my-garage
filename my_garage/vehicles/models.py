import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel
from djchoices import DjangoChoices, ChoiceItem

from my_garage.clients.models import Client
from django.utils.translation import gettext_lazy as _


class Vehicle(TimeStampedModel):
    class LastOwnerGenre(DjangoChoices):
        MALE = ChoiceItem("MALE")
        FEMALE = ChoiceItem("FEMALE")
        OTHER = ChoiceItem("OTHER")

    class Types(DjangoChoices):
        CAR = ChoiceItem("CARS")
        MOTORCYCLE = ChoiceItem("MOTORCYCLES")
        TRUCK = ChoiceItem("TRUCKS")

    class Gear(DjangoChoices):
        AUTOMATIC = ChoiceItem("AUTOMATIC")
        MANUAL = ChoiceItem("MANUAL")

    id = models.UUIDField(db_column="ID", default=uuid.uuid4, editable=False, primary_key=True)
    type = models.CharField(db_column="TYPE", null=False, blank=False, max_length=11, choices=Types)
    fipe_code = models.CharField(db_column="FIPE_CODE", null=False, blank=False, max_length=50)
    purchase_value = models.FloatField(db_column="PURCHASE_VALUE",
                                       null=False,
                                       blank=False)
    purchase_datetime = models.DateTimeField(db_column="PURCHASE_DATETIME", null=False, blank=False)
    fipe_value_on_create = models.FloatField(db_column="FIPE_VALUE_ON_CREATE",
                                             null=False,
                                             blank=False)
    brand = models.CharField(db_column="BRAND", max_length=255, null=False, blank=False)
    code_brand = models.CharField(db_column="CODE_BRAND", null=False, blank=False, max_length=100)
    model = models.CharField(db_column="MODEL", max_length=255, null=False, blank=False)
    code_model = models.CharField(db_column="CODE_MODEL", null=False, blank=False, max_length=100)
    year = models.IntegerField(db_column="YEAR", null=False, blank=False)
    model_year = models.IntegerField(db_column="MODEL_YEAR", null=False, blank=False)
    model_year_id = models.CharField(db_column="MODEL_YEAR_ID", null=False, blank=False, max_length=100)
    fuel = models.CharField(db_column="FUEL", max_length=255, null=False, blank=False)
    fuel_acronym = models.CharField(db_column="FUEL_ACRONYM", max_length=10, null=False, blank=False)
    tag = models.CharField(db_column="TAG", max_length=7, null=False, blank=False)
    client = models.ForeignKey(Client, db_column="CLIENT_ID", on_delete=models.CASCADE, null=False, blank=False)
    is_sold = models.BooleanField(db_column='IS_SOLD', default=False, null=False, blank=False)
    km = models.IntegerField(db_column="KM", null=False, blank=False)
    has_extra_key = models.BooleanField(db_column="HAS_EXTRA_KEY", null=False, blank=False)
    has_owner_handbook = models.BooleanField(db_column="HAS_OWNER_HANDBOOK", null=False, blank=False)
    gear = models.CharField(db_column="GEAR", choices=Gear, null=False, blank=False, max_length=9)
    is_unique_old_owner = models.BooleanField(db_column="IS_UNIQUE_OLD_OWNER", null=False, blank=False)
    last_owner_genre = models.CharField(db_column="LAST_OWNER_GENRE",
                                        null=True,
                                        blank=False,
                                        max_length=6,
                                        choices=LastOwnerGenre,
                                        default=None)
    has_vng = models.BooleanField(db_column="HAS_VNG", null=False, blank=False, default=False)
    engine_capacity = models.IntegerField(db_column="ENGINE_CAPACITY", null=False, blank=False)
    cylinders = models.IntegerField(db_column="CYLINDERS", null=False, blank=False)

    class Meta:
        db_table = 'VEHICLE'
        verbose_name = _('vehicle')
        verbose_name_plural = _('vehicles')
        unique_together = ["tag", "client"]
