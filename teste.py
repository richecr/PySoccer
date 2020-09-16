from py_football_data.leagues.LeagueBase import LeagueBase


league = LeagueBase()
test = league.leaderboard('england_premier_league')

for t in test.teams:
    print(t)
