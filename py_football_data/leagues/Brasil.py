from .LeagueBase import LeagueBase
from ..constants.urls import urls


class Brasil(LeagueBase):
    def __init__(self):
        super().__init__(urls.get_url_brasil_serie_a())
