from typing import List
from bs4.element import Tag
from bs4 import BeautifulSoup

from ..models.Leaderboard import Leaderboard
from ..models.TeamOnLeaderboard import TeamOnLeaderboard
from ..utils.api import Api


class LeagueBase:
    def __init__(self, url: str):
        self.api = Api()
        self.url = url

    def request_page(self) -> BeautifulSoup:
        page = self.api.get(self.url)
        return BeautifulSoup(page.text, "html.parser")

    def leaderboard(self, ano: str = "2020"):
        soup = self.request_page()
        div: List[Tag] = soup.find_all("div", {"class": "responsive-table"})
        table = div[0]
        tbody: List[Tag] = table.find_all("tbody")

        leaderboard = Leaderboard()
        soup_leaderboard = tbody[0].find_all("tr")

        ranks = range(1, len(soup_leaderboard) + 1)
        for soup_team, rank in zip(soup_leaderboard, ranks):
            team = self.__get_team(soup_team, rank)
            leaderboard.add_team(team)

        return leaderboard

    def __get_text_tag_a(self, tag_parent: Tag) -> str:
        tags_a = tag_parent.find_all('a')
        text = ""
        if (len(tags_a) == 0):
            text = "0"
        else:
            text = tags_a[0].text

        return text

    def __verify_data(self, data):
        if (data == "-"):
            return "0"

        return data

    def __get_team(self, soup_team, rank: int) -> TeamOnLeaderboard:
        soup_team = soup_team.find_all('td')

        name = self.__get_text_tag_a(soup_team[2])
        games = int(self.__get_text_tag_a(soup_team[3]))
        wins = int(self.__get_text_tag_a(soup_team[4]))
        loss = int(self.__get_text_tag_a(soup_team[5]))
        ties = int(self.__get_text_tag_a(soup_team[6]))
        goals = soup_team[7].text
        goal_difference = int(self.__verify_data(soup_team[8].text))
        pts = int(self.__verify_data(soup_team[9].text))

        team = TeamOnLeaderboard(
            name, rank, games, wins, loss, ties, goals, goal_difference, pts)

        return team
