"Import random.."
import random


class Simulator:
    "Class that runs match simulations"
    
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1_avg = self.team1.get_avg()
        self.team2_avg = self.team2.get_avg()
        self.team1_motivation = self.team1.get_motivation()
        self.team2_motivation = self.team2.get_motivation()

        self.time = 0
        self.final_score = (0,0)
        self.team1_goal_scorers = []
        self.team1_goal_scorers_by_names = []
        self.team2_goal_scorers = []
        self.team2_goal_scorers_by_names = []
        
    def to_nearest(self, number: float):
        "convert decimal number to it's nearest form (1.58 => 2), (1.23 => 1)"
        integer, dec_points = str(number).split(".")
        
        integer = int(integer)
        if int(dec_points[0]) >= 5:
            integer += 1
        
        return integer
        
    def simulate_scores(self):
        # formula = ((avg +motivation)/2)%random.randint(11, 13)
        team1_score_t1 = ((self.team1_motivation+self.team1_avg)/2)%random.randint(1, self.team1_avg//10)
        team1_score_t2 = ((self.team1_motivation+self.team1_avg)/2)%random.randint(1, self.team1_avg//10)
        
        team2_score_t1 = ((self.team2_motivation+self.team2_avg)/2)%random.randint(1, self.team1_avg//10)
        team2_score_t2 = ((self.team2_motivation+self.team2_avg)/2)%random.randint(1, self.team1_avg//10)
        
        team_1_finalscore = (team1_score_t1+team1_score_t2)/3
        team_2_finalscore = (team2_score_t1+team2_score_t2)/3
        
        team_1_finalscore = self.to_nearest(team_1_finalscore)
        team_2_finalscore = self.to_nearest(team_2_finalscore)
            
        self.final_score = (team_1_finalscore, team_2_finalscore)
    
    def simulate_goal_scorers(self):
        "method that simulate all goal scorers in a match"
        scores = self.final_score
        team_1_score, team_2_score = scores
        
        if team_1_score:
            for x in range(team_1_score):
                goal_scorrer = random.choice(self.team1.players)
                self.team1_goal_scorers.append(goal_scorrer)
                self.team1_goal_scorers_by_names.append(goal_scorrer.name)
        if team_2_score:  
            for x in range(team_2_score):
                goal_scorrer = random.choice(self.team2.players)
                self.team2_goal_scorers.append(goal_scorrer)
                self.team2_goal_scorers_by_names.append(goal_scorrer.name)
                
    def config_players(self):
        "add goals to all goal scorres"
        for ply in self.team1_goal_scorers:
            ply.G += 1
        for ply in self.team2_goal_scorers:
            ply.G += 1
            
    def config_teams(self):
        "add W, D, L, GA, GD, PTS to teams after simulation"
        self.team1.P += 1
        self.team2.P += 1
        if self.final_score[0] > self.final_score[1]:
            self.team1.W += 1
            self.team2.L += 1
        elif self.final_score[0] < self.final_score[1]:
            self.team2.W += 1
            self.team1.L += 1
        else:
            self.team1.D += 1
            self.team2.D += 1
        self.team1.GF += self.final_score[0]
        self.team1.GA += self.final_score[1]
        self.team2.GF += self.final_score[1]
        self.team2.GA += self.final_score[0]
        
    def show_results(self):
        "method that displys results after simulation"
        print(f"{self.team1.name} {self.final_score[0]} : {self.final_score[1]} {self.team2.name}")
        print(f"Team 1 scorers : {self.team1_goal_scorers_by_names}")
        print(f"Team 2 scorers : {self.team2_goal_scorers_by_names}")
                        
    def simulate(self):
        "method to start simulation"
        self.simulate_scores()
        self.simulate_goal_scorers()
        self.config_players()
        self.config_teams()
