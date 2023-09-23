from gamedata import *

class Squad:
    
    def __init__(self, club):
        self.club = club
        
    def _ShowSquad(self):
        print("Player Name\tPos\tValue\tAvg")
        for player in self.club.players:
            print(f"{player.name}\t{player.pos}\t{player.value}\t{player.avg}")
    