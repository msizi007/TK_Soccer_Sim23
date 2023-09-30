import time
import random
import settings
from gamedata import *
from settings import *
from squad import Squad
from simdemo import Simulator
# from FileManager import Files
from fixtures import Fixtures
from competition import League
from transfers import Transfers
# from tabulate import tabulate

# NEXT UPDATE
# download game data (players, teams, etc..) as json data.
# [AI PART] - AUTO
# make sure team can transfer list players, release, 
# make for loan

# MANUALS
# contacts: free, contract list: years etc.


# OPTIONS
MAIN_MENU = f'''
{DAY} {MONTH} {YEAR}
{"Team Playing" if IS_MY_TEAM_PLAYING else "Skip!"}

1   > Go to next match
2   > Squad
3   > Competition
4   > Transfers
5   > News
...more soon...
'''
# set-up
TRANSFER_LIST = []

class Game:
    """
    Class that controls the entire game!
    """
    # assign current team
    global CURRENT_TEAM
    CURRENT_TEAM = Team_A
    
    def __init__(self):
        
        # Files
        # self.files_Obj = Files("data", "fixtures.json")
        # self.files_Obj._Load_Fixtures()
        # getting list of all fixtures
        # self.all_fixtures = self.files_Obj.all_fixtures
    
        self.main_menu = MAIN_MENU
        self.ply_club = Team_A
        
        # Fixtures
        # self.fixture_Obj = Fixtures(self.all_fixtures, self.ply_club)
        
        # objects
        self.ply_squad_Obj = Squad(self.ply_club)
        
        self.is_my_team_playing = False
        self.other_matches_playing = []
        
        self.current_fixture = None
        
    def _Update(self):
        # update_team
        global CURRENT_TEAM
        CURRENT_TEAM = self.ply_club
        
        # update fixtures
        # self.fixture_Obj.update(GAME_DATETIME)
        # self.other_matches_playing = self.fixture_Obj.other_current_fixtures
        # self.is_my_team_playing = self.fixture_Obj.isPlayerMatched
        
        # update datetime
        YEAR = GAME_DATETIME.strftime("%Y")
        MONTH = GAME_DATETIME.strftime("%B")
        DAY = GAME_DATETIME.strftime("%d")
        
        if self.is_my_team_playing:
            home_team = self.fixture_Obj.current_fixture[0]
            away_team = self.fixture_Obj.current_fixture[1]
            player_team_playing_txt = f"{home_team.name} VS {away_team.name}"
            self.current_fixture = (home_team, away_team)
            
        if self.other_matches_playing:
            other_matches_txt = ""
            for match in self.other_matches_playing:
                other_matches_txt += f"{match[0].name} VS {match[1].name}\n"
        print("***********")
        print(self.other_matches_playing)
        print("***********")
        
        # update display
        self.main_menu = f'''
{DAY} {MONTH} {YEAR}
{"Team Playing today!" if self.is_my_team_playing else "Skip! No matches to play."}
{player_team_playing_txt if self.is_my_team_playing else ""}

# OTHER MATCHES PLAYING..
{other_matches_txt if self.other_matches_playing else "None"}

1   > Go to next match
2   > Squad
3   > Competition
4   > Transfers
5   > News
...more soon...
'''


    # load game data.. everytime the game starts
    def _LoadData(self):
        pass
    
    def _SaveData(self):
        pass
    
    def _ProceedWeek(self):
    
        day_Plus1 = datetime.timedelta(days=1)
        global GAME_DATETIME
        GAME_DATETIME += day_Plus1
        
        self._Run()
    
    def _Squad(self):
        self.ply_squad_Obj._ShowSquad()
        opt = input("ENTER <<PLAYER NUMBER>> OR ENTER <</BACK>> TO GO BACK!::> ")
        self._Run()

    def _League(self):
        League1 = League(ALL_CLUBS, self.ply_club)
        League1.display_LeagueTable()
        self._Run()
    
    def _Competition(self):
        pass
    
    def _News(self):
        pass
    
    def _Simulate_Other_Matches(self):
        for fxt in self.other_matches_playing:
            team1, team2 = fxt
            Simulator(team1, team2).simulate()
    
    def _Run(self):
        self._Update()
        
        print(self.main_menu)
        print(f"\n{[(clb.name, clb.P) for clb in ALL_CLUBS]}\n")
        inp = input(">> ")
        if inp == "1":
            # simulate all other matches
            self._Simulate_Other_Matches()
            if not self.is_my_team_playing:
                self._ProceedWeek()
            else:
                sim = Simulator(self.current_fixture[0], self.current_fixture[1])
                sim.simulate()
                sim.show_results()
                self._ProceedWeek()
        elif inp == "2":
            self._Squad()
        elif inp == "3":
            self._League()
        elif inp == "4":
            self._Update()
            Transfers(CURRENT_TEAM).Show_TransferList()
            self._Run()
        

SoccerSimulator = Game()
SoccerSimulator._Run()
