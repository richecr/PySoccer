from typing import List
from py_football_data.models.TeamOnLeaderboard import TeamOnLeaderboard


class Leaderboard:
    def __init__(self):
        self.teams: List[TeamOnLeaderboard] = []

    def add_team(self, team: TeamOnLeaderboard):
        self.teams.append(team)
