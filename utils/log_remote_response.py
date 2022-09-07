from logging import getLogger

from requests import Response

_logger = getLogger("__name__")


def log_remote_response(response: Response, logger=_logger):
    request = response.request
    fail_to_response_body = False
    try:
        response_body = response.json()
    except Exception as e:
        logger.info(f"Failed to get response body. {e}")
        response_body = {}
        fail_to_response_body = True

    message = (f"Remote request error. Request(body={request.body}, headers={request.headers}, url={request.url}), "
               f"Response(status={response.status_code}, body={response_body}, fails={fail_to_response_body})")

    if not response.ok:
        logger.warning(message)

    logger.info(message)
