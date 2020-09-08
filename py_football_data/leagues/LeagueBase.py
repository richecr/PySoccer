import requests
from requests.adapters import Response
from bs4 import BeautifulSoup

from ..utils.api import Api

from typing import Dict


class LeagueBase:
    def __init__(self, url: str):
        self.api = Api()
        self.url = url

    def request_page(self) -> BeautifulSoup:
        page = self.api.get(self.url)
        return BeautifulSoup(page.text, "html.parser")
