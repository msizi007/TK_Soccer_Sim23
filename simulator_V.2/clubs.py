
class Club:
    def __init__(self, name, short_name, league, stadium, manager, players=[], avg=50):
        self.name = name
        self.short_name = short_name
        self.stadium = stadium
        self.manager = manager
        self.players = players
        self.avg = avg
        self.W = 0
        self.D = 0
        self.L = 0
        self.GF = 0
        self.GA = 0
        self.GD = 0
        self.PTS = 0
        
    def ConfigLogs(self):
        self.GD = self.GF - self.GA
        self.PTS = (self.W * 3) + self.D
        
    def AddPlayer(self, player):
        self.players.append(player)
        
    def AddPlayers(self, players):
        self.players = [player for player in players]
        
    def AddWin(self, score: tuple):
        min_score, max_score = min(score), max(score)
        if min_score < max_score:
            self.W += 1
            self.GA += min_score
            self.GF += max_score
        else:
            print("ERROR: AddWin must take a score that is not equal")
        
    def AddDraw(self, score: tuple):
        min_score, max_score = min(score), max(score)
        if min_score == max_score:
            self.D += 1
            self.GA += max_score
            self.GF += min_score
        else:
            print("ERROR: AddDraw must have a score that is equal")
        
    def AddLose(self, score: tuple):
        min_score, max_score = min(score), max(score)
        if min_score < max_score:
            self.L += 1
            self.GA += max_score
            self.GF += min_score
        else:
            print("ERROR: AddLose must take a score that is not equal")
        
    