from bs4 import BeautifulSoup

from ..utils.api import Api


class LeagueBase:
    def __init__(self, url: str):
        self.api = Api()
        self.url = url

    def request_page(self) -> BeautifulSoup:
        page = self.api.get(self.url)
        return BeautifulSoup(page.text, "html.parser")
