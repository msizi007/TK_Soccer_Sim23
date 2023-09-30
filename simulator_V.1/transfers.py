from gamedata import *
from settings import *
import random

# Doc
"""
Reasons for transfer listing players:
1. transfer listed by team
2. contract is expiring

Reasons team transfer list players (contract hadn't expired.):
1. few or no appearance of player in matches
2. bad perfomance of player
3. team is not financially stable
4. player is the worst
5. team has many players and player is not that much needed
"""

from settings import TRANSFER_LIST
from gamedata import ALL_CLUBS
from settings import CURRENT_TEAM
from contracts import Contract
        
LONGEST_NAME_LENGTH = 12
class Transfers:
    def __init__(self, players_team):
        self.all_clubs = ALL_CLUBS
        self.current_team = players_team
        # exclude player's current club from list
        # self.all_clubs.remove(CURRENT_TEAM)
        
    # func that will generate list of players that
    # will be on transfer list
    def _Generate_Transferable_Players(self):
        for club in self.all_clubs:
            # checking if club has enough players
            if club.number_of_players >= 3:
                # if club is not player's club then proceed
                if club != self.current_team:
                    club.generate_transfer_listed_players()
                
    # function for showing all players on transfer list
    def Show_TransferList(self):
        TRANSFER_LIST.clear()   # clear transfer list before generating
        self._Generate_Transferable_Players() # generate transfer list
        # shuffle list
        random.shuffle(TRANSFER_LIST)
        n_space= " " * 16
        a_space = " " * 6
        print(f"Num\tName{n_space}Club{n_space}Avarage{a_space}Value")
        a_space += " " * 5
        for i, ply in enumerate(TRANSFER_LIST, start=1):
            n_space = " " * (20-len(ply.name)) # space after player name
            c_space = " " * (20-len(ply.club.name)) # space after club name
            
            print(f"{i}\t{ply.name}{n_space}{ply.club.name}{c_space}{ply.avg}{a_space}{ply.value}")
        
        print("ENTER PLAYER NUMBER TO START NEGOTIATION OR PRESS ENTER TO GO BACK TO MAIN MENU!")
        opt = input("::> ")
        
        if opt.strip() != "":
            chosen_player = TRANSFER_LIST[int(opt)-1]
            print(chosen_player)
            print(self.current_team)
            Contract(self.current_team).Set_Contract(chosen_player)
            self.Show_TransferList()