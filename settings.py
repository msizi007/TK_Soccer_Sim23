import datetime

# ALERT!: DO NOT IMPORT GAMEDATA AS THIS FILE IS MAIN SEVER..

# game date-time
GAME_DATETIME = datetime.date(2022, 3, 1)
YEAR = GAME_DATETIME.strftime("%Y")
MONTH = GAME_DATETIME.strftime("%B")
DAY = GAME_DATETIME.strftime("%d")

# game constants
ALL_PLAYERS = []
ALL_CLUBS = []

# Player's info
CURRENT_TEAM = None

# fixtures
ALL_FIXTURES = []
TEAMS_PLAYING = []
IS_MY_TEAM_PLAYING = False

# Transfers
TRANSFER_LIST = []