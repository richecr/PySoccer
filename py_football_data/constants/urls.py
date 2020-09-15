class Urls:
    url_main = "https://www.transfermarkt.com.br"

    def get_url_brazil_serie_a(self):
        return "{0}/serie-a/startseite/wettbewerb/BRA1".format(self.url_main)

    def get_url_leaderboard_complete_brazil_serie_a(self, ano: str = "2020"):
        url = self.url_main + "/campeonato-brasileiro-serie-a/tabelle/" + \
            "wettbewerb/BRA1/saison_id/" + ano

        return url

    def get_url_spain_laliga_a(self):
        return "{0}/la-liga/startseite/wettbewerb/ES1".format(self.url_main)

    def get_url_leaderboard_complete_spain(self, ano: str):
        return "{0}/primera-division/tabelle/wettbewerb/ES1/saison_id/{1}"\
            .format(
                self.url_main, ano
            )


urls = Urls()
