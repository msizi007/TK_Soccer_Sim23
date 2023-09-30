# IMPORTS
from datetime import date, timedelta
from clubs import Club
from players import Player

# CONSTS
Options = """"
1   :> Proceed Day
2   :> Squad
3   :> Tastics
4   :> News
5   :> Finances
6   :> Transfers
7   :> Data Hub
"""



# CLUBS
ClubA = Club(name="Club A", short_name="CLA", league="MAJOR", stadium="A STAD.", manager="MR A", avg=80)
ClubB = Club(name="Club B", short_name="CLB", league="MAJOR", stadium="B STAD.", manager="MR B", avg=92)
ClubC = Club(name="Club C", short_name="CLC", league="MAJOR", stadium="C STAD.", manager="MR C", avg=76)
ClubD = Club(name="Club D", short_name="CLD", league="MAJOR", stadium="D STAD.", manager="MR D", avg=83)

FIXTURES = [
    {date(2023, 4, 4):  [(ClubA, ClubB, "A Stad."), (ClubC, ClubD, "B Stad.")]},
    {date(2023, 4, 12):  [(ClubB, ClubC, "A Stad."), (ClubD, ClubA, "B Stad.")]},
    {date(2023, 4, 20):  [(ClubC, ClubD, "A Stad."), (ClubA, ClubB, "B Stad.")]},
    {date(2023, 4, 26):  [(ClubD, ClubA, "A Stad."), (ClubB, ClubC, "B Stad.")]}
]


class Fixture:
    def __init__(self, current_date, manager_team):
        self.current_date = current_date
        self.fixtures = FIXTURES

    def isPlayingToday(self):
        for ftx in self.fixtures:
            for date, schedule in ftx.items():
                club1, club2, stadium = schedule[0]
                if (self.current_date == club1 or self.current_date == club2) and date == self.current_date:
                    return True
                club1, club2, stadium = schedule[1]
                if (self.current_date == club1 or self.current_date == club2) and date == self.current_date:
                    return True
        return False


NATION_A = None

A = Player(fullname="A", age=20, pos="GK", value=1200000, squad_num=16, club=ClubA, nationality=NATION_A, isNationalPlayer=False, 
           avg=70, potential=82, contract_expiring=None)

class Game:

    def __init__(self):
        self.MANAGER_CLUB = ClubA
        self.CURRENT_DATE = date(2023, 4, 1)
        self.FORMATED_DATE = self.CURRENT_DATE.strftime("%d %b %Y")

    def MainMenu(self):
        print(self.FORMATED_DATE)
        print(f"{self.MANAGER_CLUB.name} PLAYING." if Fixture(self.CURRENT_DATE, self.MANAGER_CLUB).isPlayingToday())
        print(Options)
        opt = input("::> ")
        if opt.strip() == "1":
            self.ProceedDay()

    def ProceedDay(self):
        self.CURRENT_DATE += timedelta(days=1)
        self.FORMATED_DATE = self.CURRENT_DATE.strftime("%d %b %Y")
        self.MainMenu()

SoccerSim = Game()
SoccerSim.MainMenu()