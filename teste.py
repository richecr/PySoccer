from py_football_data.leagues.Spain import Spain
from py_football_data.leagues.Brasil import Brasil

# b = Brasil()
# s = b.leaderboard()

# for t in s.teams:
#     print(t)

spain = Spain()
s = spain.leaderboard()

for t in s.teams:
    print(t)
# print(s)
