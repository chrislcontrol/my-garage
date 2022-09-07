from logging import getLogger

import requests
from requests import Response

from my_garage.settings import PARALELLUM_V2_BASEURL
from my_garage.vehicles.models import Vehicle
from utils.log_remote_response import log_remote_response

logger = getLogger("__name__")


class FipeProvider:
    def __init__(self):
        self.base_url = PARALELLUM_V2_BASEURL
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/104.0.0.0 Safari/537.36"
        }

    def get_fipe_info(self, vehicle_type: Vehicle.Types, brand_id: str, model_id: str, year_id: str) -> Response:
        url = f"{self.base_url}/{vehicle_type}/brands/{brand_id}/models/{model_id}/years/{year_id}"
        response = requests.get(url=url, headers=self.headers)

        log_remote_response(response, logger=logger)
        return response
