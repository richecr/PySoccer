from typing import List
from .TeamOnLeaderboard import TeamOnLeaderboard


class Leaderboard:
    def __init__(self):
        self.teams: List[TeamOnLeaderboard] = []

    def add_team(self, team: TeamOnLeaderboard):
        self.teams.append(team)
