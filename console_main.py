import time
import random
import settings
from gamedata import *
from settings import *
from squad import Squad
from simdemo import Simulator
from FileManager import Files
from fixtures import Fixtures
from competition import League
from transfers import Transfers

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
        self.files_Obj = Files("data", "fixtures.json")
        self.files_Obj._Load_Fixtures()
        # getting list of all fixtures
        self.all_fixtures = self.files_Obj.all_fixtures
    
        self.main_menu = MAIN_MENU
        self.ply_club = Team_A
        
        # Fixtures
        self.fixture_Obj = Fixtures(self.all_fixtures, self.ply_club)
        
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
        self.fixture_Obj.update(GAME_DATETIME)
        self.other_matches_playing = self.fixture_Obj.other_current_fixtures
        self.is_my_team_playing = self.fixture_Obj.isPlayerMatched
        
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
# help("Game")
# 21 rows, 9 coloumns
# goalkepper net = 1 row, 3coloums(4, 5, 6)
# Try matrix soccer!ssss
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]
# [[], [], [], [], [], [], [], [], []]



"""
my_team_name = input('name your team: ')
opp_team_names = ['ice slayers' , 'crazy cats' , 'red devils' , 'blue walls']
opp_team_name = random.choice(opp_team_names)
print('your match is against {}'.format(opp_team_name))
pass_text = [' gives the ball to ' , ' passes it to ' , ' sharply gives it to ' , ' puts it in the path of ']
defend_text = [' performs a great tackle ' , ' comes up with a meaty tackle ']
shoot_text = [ 'hits the ball ' , ' curls it towards the goal ' , ' shoots ']
goal = ' have scored a beauty!'
no_goal = " have missed it!"

opp_team = ['jamie' , 'kurt' , 'andy' , 'jack' , 'sam' , 'michael' , 'roberts' , 'samuel' , 'zack' , 'charlie' , ' bob']

def matchStart() :
    my_team_score = 0
    opp_team_score = 0
    match_time = 0
    print("ref blows the whistle and we're under way!")
    while match_time < 10 :
        goal_or_not = random.randint(0,1)
        whose_ball = random.randint(0,1)
        if whose_ball == 0 :
            time.sleep(2)
            print("the ball is taken and {} {} {} {} ".format(random.choice(opp_team),random.choice(pass_text),random.choice(opp_team),random.choice(shoot_text)))
            time.sleep(2)
            if goal_or_not == 1 :
                print("{} score!".format(opp_team_name))
                opp_team_score += 1
                time.sleep(2)
                print(" it's {} {} ".format(str(my_team_score) , str(opp_team_score)))
                match_time += 1
            else :
                time.sleep(2)
                print("{} {} {} {}".format(random.choice(my_team),random.choice(pass_text),random.choice(my_team),random.choice(shoot_text)))
                time.sleep(2)
                print("{} {}!".format(opp_team_name,no_goal))
                match_time += 1
        else :
            if goal_or_not == 1 :
                    time.sleep(2)
                    print("{} {} {} {}".format(random.choice(my_team),random.choice(pass_text),random.choice(my_team),random.choice(shoot_text)))
                    time.sleep(2)
                    print("{} {}!".format(my_team_name,goal) )
                    my_team_score += 1
                    time.sleep(2)
                    print(" it's {} {} ".format(str(my_team_score) , str(opp_team_score)))
                    match_time += 1
            else :
                    time.sleep(2)
                    print("{} {} {} {}".format(random.choice(my_team),random.choice(pass_text),random.choice(my_team),random.choice(shoot_text)))
                    time.sleep(2)
                    print("{} {}!".format(my_team_name,no_goal))
                    time.sleep(2)
                    match_time += 1

    if my_team_score > opp_team_score :
        print("{} {} {} win!".format(my_team_score,opp_team_score,my_team_name))
    elif my_team_score < opp_team_score :
        print("{} {} {} win!".format(my_team_score,opp_team_score,opp_team_name))
    else :
        print("{} {} It's a tie".format(my_team_score,opp_team_score))

manager_name = input('enter name of manager: ')
print('hi {} , you have $120 million dollars to start with and build your very own dream team .'\
"you can buy 11 players.listed player prices are in million ".format(manager_name))

my_budget = 120
players = {'hart': 20 ,'curtois': 18 ,'navas': 20 ,'bravo': 15,'cech': 15 ,'de gea': 20 , 'ramos': 40 , 'pique': 30 , 'ronaldo': 50 ,
'messi': 50 , 'suarez': 45 , 'neymar': 48 , 'bale': 45 , 'hazard': 42 , 'aguero': 40 , 'smith': 2 , 'johhny': 4 , 'sunny': 8 , 'patrick': 5,
'debian': 3 , 'shaggy': 4.5 , 'randy': 3 , 'karim': 6 , 'samuel':2 , 'billy':4 , "aaron":5 }
my_team = []

for key,value in players.items():
    print("Name: {} Value: {} Million Dollars".format(key,value))

while len(my_team) < 11:
    buy_player = input('name player to buy: ')
    if buy_player in my_team:
        print(buy_player + " is already in your team")
        continue
    if buy_player not in players:
        print('that player is not available for transfer . check the transfer list again')
        continue
    print("Player: {} Value: {} Million Dollars; {}'s Budget: {} Million Dollars".format(buy_player, players[buy_player], manager_name, my_budget))
    ask_final = input('are you sure you want to make this purchase ? (yes or no) , this cannot be reversed; ')
    if ask_final.lower() != "yes":
        continue
    if my_budget - players[buy_player] <= 0:
        print("insufficient funds")
        ask_to_sell = input('you need to sell players , enter name of player to sell')
        if ask_to_sell not in my_team :
            continue
        print("{} ,  Value: {} Million Dollars.Sold ".format(ask_to_sell,players[buy_player]))
        my_team.remove(ask_to_sell)
        my_budget += players[ask_to_sell]
        print("{} is your new budget".format(my_budget))
        print("you have {} players in your team".format(str(len(my_team))))
        continue
    my_budget -= players[buy_player]
    my_team.append(buy_player)
    print("you have {} players in your team".format(str(len(my_team))))

print("\n".join(my_team))
print('  This is your final team.May you achieve victory and glory with them!')


matchStart()
"""