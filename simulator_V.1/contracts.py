# Module for dealing with any types of contacts
# loans, contacts, contact with release clause, etc.abs

# contract factors :
# salary, value, years, release clause, bonus percentage
from gamedata import *
from settings import TRANSFER_LIST
import big_nums

# Updates
# fix AI:
# give player a value according to his market demand
# (demand * random value) + player value => given value
# club which offered highest should be priority

class Contract:
    def __init__(self, ply_club):
        self.all_clubs = ALL_CLUBS
        self.ply_club = ply_club
        self.PENDING_CONTRACTS = []
        self.transfer_listed_players = TRANSFER_LIST
    
    def update(self):
        self.transfer_listed_players = TRANSFER_LIST
        self.PENDING_CONTRACTS = []
        
    def Set_Contract(self, player):
        if player in self.transfer_listed_players:
            self.Start_Contact_Negotiations(player)
        else:
            print("ERROR: UNREACHABLE PLAAYER.. CHECK CONTRACTS.PY ")
            
    def Start_Contact_Negotiations(self, player):
        print(f"{self.ply_club.name.upper()} BUDGET: {self.ply_club.money}")
        print()
        player_value = big_nums.shorten_value(player.value)
        transfer_listed_value = big_nums.shorten_value(player.transfer_listed_value)
        player_salary = big_nums.shorten_value(player.salary)
        print(f'''
              {self.PENDING_CONTRACTS}
|-------------------------------------------------------
|                   Player's Contract!                 |
-------------------------------------------------------|
| Name: {player.name}
| Value: {player_value}     Transfer Value(Recomended): {transfer_listed_value}
| Club: {player.club.name}   Avarage: {player.avg}    Salary: {player_salary}
|-------------------------------------------------------
''')
        # get value, salary, number of years, salary bonus
        offered_value = int(input("Value: "))
        offered_salary = int(input("Salary: "))
        offered_NOY = int(input("Number of years (1-5): "))
        
        if (offered_value >= player.value) and (offered_salary >= player.salary):
            if 1 <= offered_NOY  <= 5:
                if self.ply_club.money >= offered_value:
                    print(f"{player.name} has considered your contract and will respond next week.")
                    transfer_dict = {"from": player.club, "to": self.ply_club, "value": offered_value, "salary": offered_salary, "NOY": offered_NOY}
                    self.PENDING_CONTRACTS.append(transfer_dict)
                else:
                    print(f"{player.name}'s agent has turned down your contract as you have failed to meet the standards!..")
            else:
                print("Number of years must be between 1 and 5")
        else:
            print("Player is not interested and feels you are offering a little than expected.")

    def Auto_Simulate_Market(self):
        for clb in self.all_clubs:
            if clb != self.ply_club:
                player = random.choice(TRANSFER_LIST)
                if (player.club != clb) and (ply.transfer_listed_value >= club.money):
                    random_value = random.randint(player.value-10000000, player.value+10000000)
                    random_salary = random.randint(player.salary-50000, player.salary+50000)
                    random_NOY = random.randint(1, 5)
                    self.Auto_Negotiate_Player(clb, player, random_value, random_salary, random_NOY)
                    
    def Auto_Negotiate_Player(self, buying_club, player, value, salary, noy):
        
        if (value >= player.value) and (salary >= player.salary):
            if 1 <= noy  <= 5:
                if buying_club.money >= value:
                    transfer_dict = {"from": player.club, "to": self.ply_club, "value": offered_value, "salary": offered_salary, "NOY": offered_NOY}
                    self.PENDING_CONTRACTS.append(transfer_dict)
                