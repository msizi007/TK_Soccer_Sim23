
class Player:
    def __init__(self, fullname, age, pos, value, squad_num, club, nationality, isNationalPlayer=False, avg=50, potential=50, 
            contract_expiring=None):
        self.fullname = fullname
        self.age = age
        self.value = value
        self.position = pos
        self.squad_num = squad_num
        self.club = club
        self.nationality = nationality
        self.isNationalPlayer = isNationalPlayer
        self.contract_expiring = contract_expiring
        # STATS
        self.AVG = avg
        # LEAGUE STATS
        self.GOALS = 0
        self.ASSISTS = 0
        self.APP = 0
        
        # Add player to the club when club is given
        self.club.AddPlayer(self)
        
    def GetAvg(self):
        return self.AVG
    
    def AddGoals(self, goals):
        self.GOALS += goals
        
    def AddAssists(self, assists):
        self.ASSISTS += assists