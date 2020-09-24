from PySoccer.leagues.LeagueBase import LeagueBase


league = LeagueBase()
test = league.leaderboard('portugal_nos_league', 2019)

for t in test.teams:
    print(t)
