import requests
import logging
import re
import os

SESSION = requests.Session()

APP_URL = os.getenv("APP_URL", "")
ACCESS_KEY = os.getenv("ACCESS_KEY", "")

LOG = logging.getLogger()
