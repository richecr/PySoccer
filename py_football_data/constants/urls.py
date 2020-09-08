class Urls:
    url_main = 'https://www.transfermarkt.com.br/'

    def get_url_brasil_serie_a(self):
        return '{0}serie-a/startseite/wettbewerb/BRA1'.format(self.url_main)


urls = Urls()
