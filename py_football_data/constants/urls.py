class Urls:
    url_main = "https://www.transfermarkt.com.br"

    def get_url_brazil_serie_a(self):
        return "{0}/serie-a/startseite/wettbewerb/BRA1".format(self.url_main)

    def get_url_table_complete_brazil_serie_a(self, ano: str = "2020"):
        url = self.url_main + "/campeonato-brasileiro-serie-a/tabelle/" + \
            "wettbewerb/BRA1/saison_id/" + ano

        return url


urls = Urls()
