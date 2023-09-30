from settings import ALL_CLUBS
from settings import CURRENT_TEAM

# Properties
# name, manager, captain, W, L, D, GA, GF, PTS
#
class Club:
    def __init__(self, name, manager, money):
        self.name = name
        self.manager = manager
        self.players = []
        self.number_of_players = len(self.players)
        
        self.captain = None
        self.motivation = 0
        
        # scores and ratings
        self.P = 0
        self.W = 0
        self.D = 0
        self.L = 0
        self.GA = 0
        self.GF = 0
        self.GD = 0
        self.PTS = 0
        
        # finances
        self.value = 0
        self.money = money        
        
        # register club
        global ALL_CLUBS
        ALL_CLUBS.append(self)
    
    def _Transfer_list(self, player):
        player.transfer_list()
        
    def _Add_player(self, player):
        self.players.append(player)
        self._Update()
        
    def _Update(self):
        self.number_of_players = len(self.players)
        self.set_avg()
        self.set_captain()
        self.set_motivation()
    
    def get_worst_players(self, number_of_players):
        Players_copy_list = self.players.copy()
        Worst_players_list = []
        for x in range(number_of_players+1):
            # set worst player: default = fisrt on the list
            worst_player = Players_copy_list[0]
            for ply in Players_copy_list:
                if ply.avg < worst_player.avg:
                    worst_player = ply
            # remove worst player from players copy list
            Players_copy_list.remove(worst_player)
            # add player to worst players list
            Worst_players_list.append(worst_player)
        # return worst players list
        return Worst_players_list
    
    def generate_transfer_listed_players(self):
        self._Update()
        listed_players = self.get_worst_players(1)
        for ply in listed_players:
            ply.transfer_list()  
             
    def set_motivation(self):
        self.set_captain()
        self.motivation = self.captain.avg
        
    def get_motivation(self):
        self.set_motivation()
        return self.motivation
            
    def set_captain(self):
        best_avg = 0
        top_player = None
        # captain is player with highhest avg(avarage)
        for ply in self.players:
            if ply.avg > best_avg:
                top_player = ply
                best_avg = ply.avg
        self.captain = top_player
        
    def get_captain(self):
        self.set_captain()
        return self.captain
        
    def set_avg(self):
        total = 0
        for player in self.players:
            total += player.avg
        self.avg = round((total/self.number_of_players), 3)
        return self.avg
    
    def get_avg(self):
        self.set_avg()
        return self.avg
    
    def fire_manager(self):
        self.manager = None
        
    def hire_manager(self, new_manager):
        # if club doesn't have manager then hire one
        if not self.manager:
            self.manager = new_manager
      