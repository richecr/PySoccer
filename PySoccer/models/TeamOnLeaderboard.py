class TeamOnLeaderboard:
    def __init__(
        self, name: str, rank: int, games: int, wins: int, loss: int,
        ties: int, goals: str, goal_difference: int, points: int,
    ):
        self.name = name
        self.rank = rank
        self.games = games
        self.wins = wins
        self.loss = loss
        self.ties = ties
        self.goals = goals
        self.goal_difference = goal_difference
        self.points = points

    def __str__(self) -> str:
        return str(self.rank) + " - " + self.name + " - " + str(self.games) + \
            " - " + str(self.wins) + " - " + str(self.loss) + " - " + \
            str(self.ties) + " - " + self.goals + " - " + \
            str(self.goal_difference) + " - " + str(self.points)
