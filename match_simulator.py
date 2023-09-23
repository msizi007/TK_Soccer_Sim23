import random
from gamedata import *

# EXPLAINATION!
"""
Simulator is a module for simulating matches between two
teams. 

# Factors
    - Key_players, Team_avarage, Coaching, playing_style,
    - Formation
"""

class Simulator:
    def __init__(self):
        self.team1 = None
        self.team2 = None
        self.team1_chance = 0
        self.team2_chance = 0
    
    def simulate(self, team1, team2):
        self.team1, self.team2 = team1, team2
        
        if team1.avg > team2.avg:
            self.team1_chance = (team1.avg//10)
            self.team2_chance = ((team1.avg-team2.avg)//10)
        elif team2.avg > team1.avg:
            self.team2_chance = (team2.avg//10)
            self.team1_chance = ((team2.avg-team1.avg)//10)
        else:
            # getting number of chances..
            self.team1_chance = (team1.avg//10)
            self.team2_chance = (team2.avg//10)
            
        # randomising chances
        self.team1_chance -= random.randint(1, self.team1_chance)
        self.team2_chance -= random.randint(1, self.team2_chance)
            
        print(self.team1_chance, self.team2_chance)

o = Simulator()
o.simulate(Team_A, Team_B)
print(Team_A.avg, Team_B.avg)





