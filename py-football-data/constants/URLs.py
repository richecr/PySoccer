class Urls:
    url_main = 'https://www.transfermarkt.com.br/'

    @staticmethod
    def get_url_brasil_serie_a():
        return '${url_main}serie-a/startseite/wettbewerb/BRA1'.format(url_main)
