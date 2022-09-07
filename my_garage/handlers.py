from requests import Response
from rest_framework.views import exception_handler

from utils.errors_formatter import ErrorsFormatter


def exception_errors_format_handler(exc, context):
    response = exception_handler(exc, context)

    # If an unexpected error occurs (server error, etc.)
    if response is None:
        return response

    formatter = ErrorsFormatter(exc)

    response.data = formatter()

    return response


def handle_response_body(response: Response):
    try:
        return response.json()
    except Exception:
        return {}
