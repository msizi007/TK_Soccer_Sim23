# imports
from gamedata import *
from settings import *

class Fixtures:
    def __init__(self, all_fixtures, players_club):
        self.all_fixtures = all_fixtures
        self.all_clubs = ALL_CLUBS.copy()
        self.players_club = players_club
        self.isPlayerMatched = False
        
        self.current_date = None
        self.player_current_fixture = None
        self.other_current_fixtures = []
        
        self.current_fixture = None # (team1, team2)

    def update(self, date):
        
        # default values
        self.isPlayerMatched = False
        self.current_fixture = None
        self.player_current_fixture = None
        self.other_current_fixtures = []
        
        # other values
        self.current_date = date
        self.update_fixtures()
        
    def update_fixtures(self):
        for fxt in self.all_fixtures:
            team1, team2, playingDate = fxt
            if ((team1 == self.players_club.name) or (team2 == self.players_club.name)) and playingDate == self.current_date:
                self.isPlayerMatched = True
                self.current_fixture = [team1, team2]
                self.current_fixture = self.get_as_object(team1, team2)
            elif playingDate == self.current_date:
                fixture_as_obj = self.get_as_object(team1, team2)
                if fixture_as_obj not in self.other_current_fixtures:
                    self.other_current_fixtures.append(fixture_as_obj)
        # function that takes data as names(team_1, team_2) and
    # set respective objects.. (<...>, <....>)  
    # need to fix : when config home/away match          
    def get_as_object(self, team_1_name, team_2_name):
        object_data = []
        for c in self.all_clubs:
            if c.name == team_1_name:
                object_data.append(c)
            elif c.name == team_2_name:
                object_data.append(c)
        return object_data

"""
from FileManager import Files
G = Files("data", "fixtures.file")
G._Load_Fixtures()
all_fxt = G.all_fixtures

from datetime import date
Y = Fixtures(all_fxt, Team_B)
Y.update(date(2005, 6, 15))
print(Y.other_current_fixtures)
print(Y.current_fixture)
"""