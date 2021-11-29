import requests
from lib.utils import build_request_headers
from config import SESSION, LOG


class Latest:

    def __init__(self):
        self.latest_url = "/latest"

    def check_latest_rate(self, app_url, access_key):
        LOG.info("check rate")
        payload = {"access_key": access_key, "base": "USD",
        "symbols": "GBP,JPY,EUR"}
        response = SESSION.get(
            f"{app_url}{self.latest_url}", params=payload)
        return response
