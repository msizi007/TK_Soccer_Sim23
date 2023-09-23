import json
import datetime
from gamedata import *
# from settings import ALL_FIXTURES, ALL_PLAYERS
from players import Player
# from fixtures import FixtureSchedule, Fixture

# FIXES:
# Fix everything that has to do with fixtures class..abs
# fixtures will be set manually through a json file
ALL_FIXTURES = []

class Files:
    
    def __init__(self, path, filename):
        
        self.filename = filename
        self.all_players = None
        self.all_fixtures = []
        
        # if path is None (assign "") else set path
        if not path:
            self.path = ""
            self.full_filePath = self.filename
        else:
            self.path = path
            self.full_filePath = f"{self.path}/{self.filename}"
    
    def Encode_Fixtures(self, fixture_list):
        Encoded_Fixture_list = []
        for fxt in fixture_list:
                dict_data = {"team1": fxt[0].name, "team2": fxt[1].name, "date_year": fxt[2].year, "date_month": fxt[2].month, "date_day": fxt[2].day}
                Encoded_Fixture_list.append(dict_data)
        return Encoded_Fixture_list
    
    def Encode_Players(self, data_list):
        Encoded_Players_list = []
        for ply in data_list:
            if isinstance(ply, Player):
                dict_data = {"name": ply.name, "club_name": ply.club.name, "club_manager": ply.club.manager, "pos": ply.pos, "value": ply.value,"avg": ply.avg}
                Encoded_Players_list.append(dict_data)
        return Encoded_Players_list
    
    def Save_Players(self, data_list: list):
        encoded_data_list = self.Encode_Players(data_list)
        print(encoded_data_list)
        # open file and save data
        # with open(self.full_filePath, "w") as file:
        #    json.dump(encoded_data_list, file)
            
    def Save_Fixtures(self, fixture_list: list):
        
        encoded_data_list = self.Encode_Fixtures(fixture_list)
        with open(self.full_filePath, "w") as file:
            json.dump(encoded_data_list, file, indent=4)                                  
        
    # save loaded changes
    def Decode_Players(self, dict_data: dict):
        Decoded_list = []
        
        # decode data
        for ply in dict_data:
            ply_instance = Player(ply['name'], Club(ply['club_name'], ply['club_manager']), ply['pos'], ply['value'], ply['avg'])
            Decoded_list.append(ply_instance)                                  
            
            # save loaded changes
            self.all_players = Decoded_list
    
    # decode fixtures
    def Decode_Fixtures(self, fixture_data: dict):
        Decoded_list = []
        
        # decode data
        for fxt in fixture_data:
            fxt_instance = (fxt['team1'], fxt['team2'], datetime.date(fxt['date_year'], fxt['date_month'], fxt['date_day']))
            Decoded_list.append(fxt_instance)                                  
        
        # save loaded changes
        self.all_fixtures = Decoded_list
        global ALL_FIXTURES
        ALL_FIXTURES = Decoded_list
        
    def _Load_Players(self):
        with open(self.full_filePath, "r") as file:
            data = json.load(file)
        self.Decode_Players(data)
        
    def _Load_Fixtures(self):
        with open(self.full_filePath, "r") as file:
            data = json.load(file)
        self.Decode_Fixtures(data)
        

class Set_Fixture:
    def __init__(self, t1, t2, date, data=None):
        global ALL_FIXTURES
        self.t1 = t1
        self.t2 = t2
        
        self.data = (t1, t2, date)
        ALL_FIXTURES.append(self.data)
"""
Set_Fixture(Team_A, Team_B, datetime.date(2022, 3, 12))
Set_Fixture(Team_D, Team_C, datetime.date(2022, 3, 12))
Set_Fixture(Team_C, Team_A, datetime.date(2022, 3, 17))
Set_Fixture(Team_D, Team_B, datetime.date(2022, 3, 17))
Set_Fixture(Team_A, Team_C, datetime.date(2022, 3, 25))
Set_Fixture(Team_B, Team_D, datetime.date(2022, 3, 25))
Set_Fixture(Team_C, Team_B, datetime.date(2022, 3, 30))
Set_Fixture(Team_D, Team_A, datetime.date(2022, 3, 30))
Set_Fixture(Team_A, Team_B, datetime.date(2022, 4, 5))
Set_Fixture(Team_C, Team_D, datetime.date(2022, 4, 5))
Set_Fixture(Team_B, Team_A, datetime.date(2022, 3, 12))
Set_Fixture(Team_D, Team_C, datetime.date(2022, 3, 12))

Fix_Files = Files("data", "fixtures.json")
Fix_Files.Save_Fixtures(ALL_FIXTURES)

"""
Fix_Files = Files("data", "fixtures.json")
Fix_Files._Load_Fixtures()
print(ALL_FIXTURES)