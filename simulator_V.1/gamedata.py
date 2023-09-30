from players import Player
from teams import Club
from settings import ALL_CLUBS, ALL_PLAYERS

Team_A = Club("Clubin F.C", "Mc Lopern", 17000000)
Team_B = Club("Manville Utd.", "Oven Stove", 72000000)
Team_C = Club("Exo Club", "Mulan Myths", 32000000)
Team_D = Club("Forest Hill F.C", "Josse Masons", 5000000)

# Team A
Adan_Jesse = Player("Adan Jesse", Team_A, "CF", 320500, 81)
Wiz_Khadi = Player("Wiz Khadi", Team_A, "CM", 230000, 79)
Julius_Mahroo = Player("Julius Mahroo", Team_A, "WF", 540000, 87)
Barn_Bamba = Player("Barn Bamba", Team_A, "CB", 300000, 83)
Steve_Kioli = Player("Steve_Kioli", Team_A, "GK", 126000, 68)

# Team B
James_Omma = Player("James Omma", Team_B, "CF", 320500, 83)
Lazio_Marino = Player("Lazio_Marino", Team_B, "CM", 230000, 76)
Kouli_Nazli = Player("Kouli_Nazli", Team_B, "WF", 540000, 88)
Amra_Lonke = Player("Amra_Lonke", Team_B, "CB", 300000, 84)
Max_Wesley = Player("Max_Wesley", Team_B, "GK", 126000, 67)

# Team C
Egnes_Mariano = Player("Egnes_Mariano", Team_C, "CF", 320500, 81)
Covid_19 = Player("Covid_19", Team_C, "CM", 230000, 83)
Why_Virus = Player("Why_Virus", Team_C, "WF", 540000, 85)
Povic_Fali = Player("Povic_Fali", Team_C, "CB", 300000, 82)
Tuena_Tally = Player("Tuena_Tally", Team_C, "GK", 126000, 65)

# Team D
Egnes = Player("Egnes", Team_D, "CF", 320500, 81)
Covid = Player("Covid", Team_D, "CM", 230000, 83)
Virus = Player("Virus", Team_D, "WF", 540000, 85)
Povic = Player("Povic", Team_D, "CB", 300000, 82)
Tally = Player("Tally", Team_D, "GK", 126000, 65)

def _Sort_Players():
    # check all players and clubs
    # if player belongs to club the add else pass
    # Algorithm @? (Later!)
    for player in ALL_PLAYERS:
        for club in ALL_CLUBS:
            if player.club == club:
                club._Add_player(player)

_Sort_Players()