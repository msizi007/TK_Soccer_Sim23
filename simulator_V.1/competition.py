from gamedata import *
from tabulate import tabulate

class League:

    def __init__(self, teams_list, ply_club):
        self.teams_list = teams_list
        self.ply_club = ply_club
        self.sorted_clubs = []
        self.club_pts_tuple = [] # [(Club, PTS, GD), ]
        self.teams_list_copy = self.teams_list.copy()

    def _Sort_League_Points(self):
        for club in self.teams_list:
            club.P = club.W + club.L + club.D
            club.PTS = (club.W*3) + club.D
            club.GD = club.GF - club.GA

        self.teams_list_copy = self.teams_list.copy()   # copy list

    def _Sort_League_Stats(self):

        highest_ranked_club = self.teams_list_copy[0]
        for clb in self.teams_list_copy:
            if clb.PTS > highest_ranked_club.PTS:
                highest_ranked_club = clb

        self.sorted_clubs.append(highest_ranked_club)
        self.teams_list_copy.remove(highest_ranked_club)

        while self.teams_list_copy != []:
            self._Sort_League_Stats()
            
    def display_LeagueTable(self):
        self._Sort_League_Points()
        self._Sort_League_Stats() 

        teams_data = [(f"**{club.name}**" if self.ply_club == club else club.name, club.P, club.W, club.D, club.L, club.GF, club.GA, club.PTS) for club in self.sorted_clubs]
        print(tabulate(teams_data, ["Name", "P", "W", "D", "L", "GF", "GA", "PTS"], "fancy_grid"))