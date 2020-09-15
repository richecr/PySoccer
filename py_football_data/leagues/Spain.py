from .LeagueBase import LeagueBase
from ..constants.urls import urls


class Spain(LeagueBase):
    def __init__(self):
        super().__init__(urls.get_url_spain_laliga_a())

    def leaderboard(self, ano: str = "2020"):
        self.url = urls.get_url_leaderboard_complete_spain(ano)
        return super().leaderboard(ano=ano)
