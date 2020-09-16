from py_football_data.leagues.Brazil import Brazil
from py_football_data.leagues.England import England
from py_football_data.leagues.Spain import Spain


class League:
    def __init__(self):
        self.league_brazil = Brazil()
        self.league_englad = England()
        self.league_spain = Spain()

    def leaderboard_brazil(self, ano: str = "2020"):
        return ''
