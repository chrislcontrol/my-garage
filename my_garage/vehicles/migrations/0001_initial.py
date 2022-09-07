# Generated by Django 4.1.1 on 2022-09-07 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(db_column='ID', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('CARS', 'CAR'), ('MOTORCYCLES', 'MOTORCYCLE'), ('TRUCKS', 'TRUCK')], db_column='TYPE', max_length=11)),
                ('fipe_code', models.CharField(db_column='FIPE_CODE', max_length=50)),
                ('purchase_value', models.FloatField(db_column='PURCHASE_VALUE')),
                ('purchase_datetime', models.DateTimeField(db_column='PURCHASE_DATETIME')),
                ('fipe_value_on_create', models.FloatField(db_column='FIPE_VALUE_ON_CREATE')),
                ('brand', models.CharField(db_column='BRAND', max_length=255)),
                ('code_brand', models.CharField(db_column='CODE_BRAND', max_length=100)),
                ('model', models.CharField(db_column='MODEL', max_length=255)),
                ('code_model', models.CharField(db_column='CODE_MODEL', max_length=100)),
                ('year', models.IntegerField(db_column='YEAR')),
                ('model_year', models.IntegerField(db_column='MODEL_YEAR')),
                ('model_year_id', models.CharField(db_column='MODEL_YEAR_ID', max_length=100)),
                ('fuel', models.CharField(db_column='FUEL', max_length=255)),
                ('fuel_acronym', models.CharField(db_column='FUEL_ACRONYM', max_length=10)),
                ('tag', models.CharField(db_column='TAG', max_length=7)),
                ('is_sold', models.BooleanField(db_column='IS_SOLD', default=False)),
                ('km', models.IntegerField(db_column='KM')),
                ('has_extra_key', models.BooleanField(db_column='HAS_EXTRA_KEY')),
                ('has_owner_handbook', models.BooleanField(db_column='HAS_OWNER_HANDBOOK')),
                ('gear', models.CharField(choices=[('AUTOMATIC', 'AUTOMATIC'), ('MANUAL', 'MANUAL')], db_column='GEAR', max_length=9)),
                ('is_unique_old_owner', models.BooleanField(db_column='IS_UNIQUE_OLD_OWNER')),
                ('last_owner_genre', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], db_column='LAST_OWNER_GENRE', default=None, max_length=6, null=True)),
                ('has_vng', models.BooleanField(db_column='HAS_VNG', default=False)),
                ('engine_capacity', models.IntegerField(db_column='ENGINE_CAPACITY')),
                ('cylinders', models.IntegerField(db_column='CYLINDERS')),
                ('client', models.ForeignKey(db_column='CLIENT_ID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'vehicle',
                'verbose_name_plural': 'vehicles',
                'db_table': 'VEHICLE',
                'unique_together': {('tag', 'client')},
            },
        ),
    ]