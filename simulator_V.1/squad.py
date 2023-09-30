from gamedata import *
from tabulate import tabulate

class Squad:
    
    def __init__(self, club):
        self.club = club
        
    def _ShowSquad(self):
        players_data = []
        for i, player in enumerate(self.club.players, start=1):
            players_data.append((i, player.name, player.pos, f"{player.value:,}", player.avg))
        print(tabulate(players_data, ["Num", "Name", "Pos", "Value", "Avg"], "fancy_grid"))
        
    