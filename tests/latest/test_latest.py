import pytest
from lib.latest import Latest
from config import APP_URL, SESSION, LOG, ACCESS_KEY


def test_base_url():
    LOG.info("test_base_url")
    response = Latest().check_latest_rate(APP_URL, ACCESS_KEY)
    assert response.ok
