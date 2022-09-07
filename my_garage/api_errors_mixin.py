from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import exceptions as rest_exceptions
from rest_framework.exceptions import NotAuthenticated

from utils.errors_formatter import get_error_message


class ApiErrorsMixin:
    """
    Mixin that transforms Django and Python exceptions into rest_framework ones.
    without the mixin, they return 500 status code which is not desired.
    """
    expected_exceptions = {
        ValidationError: rest_exceptions.ValidationError,
        PermissionError: rest_exceptions.PermissionDenied,
        rest_exceptions.PermissionDenied: rest_exceptions.PermissionDenied,
        NotAuthenticated: NotAuthenticated,
        IntegrityError: rest_exceptions.ValidationError,
    }

    def handle_exception(self, exc):
        if isinstance(exc, tuple(self.expected_exceptions.keys())):
            drf_exception_class = self._get_exception(exc)
            drf_exception = drf_exception_class(get_error_message(exc))

            return super().handle_exception(drf_exception)

        return super().handle_exception(exc)

    def _get_exception(self, exc):
        return self.expected_exceptions[exc.__class__]
