from types import FunctionType
from typing import Dict, Callable


class UrlsLeagues:
    url_main = "https://www.transfermarkt.com.br"

    def __init__(self):
        self.urls: Dict[str, Callable[[str], str]] = {
            "brazil_serie_a": self.get_url_leaderboard_brazil_serie_a,
            "spain_laliga_a": self.get_url_leaderboard_spain,
            "england_premier_league": self.get_url_leaderboard_england
        }

    def get_url(self, championship: str, year: str = "2020"):
        return self.urls[championship](year)

    def get_url_brazil_serie_a(self):
        return "{0}/serie-a/startseite/wettbewerb/BRA1".format(self.url_main)

    def get_url_leaderboard_brazil_serie_a(self, year: str):
        url = self.url_main + "/campeonato-brasileiro-serie-a/tabelle/" + \
            "wettbewerb/BRA1/saison_id/" + year

        return url

    def get_url_spain_laliga_a(self):
        return "{0}/la-liga/startseite/wettbewerb/ES1".format(self.url_main)

    def get_url_leaderboard_spain(self, year: str):
        return "{0}/primera-division/tabelle/wettbewerb/ES1/saison_id/{1}"\
            .format(
                self.url_main, year
            )

    def get_url_england_premier_league(self):
        return "{0}/premier-league/startseite/wettbewerb/GB1".format(
            self.url_main
        )

    def get_url_leaderboard_england(self, year: str):
        return "{0}/premier-league/tabelle/wettbewerb/GB1/saison_id/{1}"\
            .format(
                self.url_main, year
            )


urls = UrlsLeagues()
