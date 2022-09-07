import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.models import TimeStampedModel
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _


class ClientManager(BaseUserManager):
    def create_superuser(self, username, email, first_name, last_name, password):
        user = self.model(username=username,
                          client_id=username,
                          email=email,
                          is_superuser=True,
                          is_staff=True,
                          first_name=first_name,
                          last_name=last_name)
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user


class Client(TimeStampedModel, AbstractUser):
    id = models.UUIDField(_("Primary Key"), db_column="ID", default=uuid.uuid4, editable=False, primary_key=True)
    first_name = models.CharField(_("first name"), db_column="FIRST_NAME", max_length=150, blank=False, null=False)
    last_name = models.CharField(_("last name"), db_column="LAST_NAME", max_length=150, blank=False, null=False)
    email = models.EmailField(_("email address"), db_column="EMAIL", blank=False, null=False)

    class Meta:
        db_table = 'CLIENT'
        verbose_name = _('client')
        verbose_name_plural = _('clients')
