from settings import ALL_PLAYERS
from settings import TRANSFER_LIST
import random

# Player class
class Player:
    def __init__(self, name, club, pos, value, avg):
        self.name = name
        self.club = club
        self.pos = pos
        self.value = value
        self.avg = avg
        
        self.transfer_listed_value = self.value + 20000
        self.salary = 0

        # PLAYER STATS
        self.P = 0
        self.G = 0  
        self.A = 0
        
        # others
        self.isTransferListed = False
        
        # add player as registered player
        global ALL_PLAYERS
        ALL_PLAYERS.append(self)
        
    # function that moves player to a new club
    def move_to(self, new_club):
        self.club = new_club
        
    def train_player(self):
        # randomly increase avg
        increase_in_training = random.random()
        self.train_player += increase_in_training
        print(f"{self.name} has increased by {increase_in_training}")

    def transfer_list(self):
        global TRANSFER_LIST
        # add player to transfer list
        TRANSFER_LIST.append(self)
        self.isTransferListed = True
        
    def remove_from_transfer_list(self):
        global TRANSFER_LIST
        if self in TRANSFER_LIST:
            TRANSFER_LIST.remove(self)
            self.isTransferListed = False
            
