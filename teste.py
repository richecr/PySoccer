from PySoccer.leagues.LeagueBase import LeagueBase


league = LeagueBase()
test = league.leaderboard('italy_serie_a')

for t in test.teams:
    print(t)
