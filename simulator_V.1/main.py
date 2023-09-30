# Imports
import tkinter as tk
from tkinter import messagebox
import datetime
# Secondary Imports
from _extras import Fonts
from gamedata import *
from teams import Club
# from players import Player
# from squad import Squad

     
# Class containing the whole game!
class Game:
    def __init__(self, size: tuple):
        # screen config
        self.size = size
        self.root = tk.Tk()
        self.config_screen()
        
        # datetime
        self.current_date = datetime.datetime(2022, 5, 1)
        self.year = self.current_date.year
        self.month = self.current_date.strftime("%b")
        self.day = self.current_date.strftime("%d")
        self.formated_date = f"Date: {self.day} {self.month} {self.year}"
        
        # Players attribute
        self.my_club = Team_A
        self.my_starting_lineup = []
        # Objects
        
    def config_screen(self):
        # screen size
        self.WIDTH, self.HEIGHT = self.size
        self.tkinter_screensize = f"{self.WIDTH}x{self.HEIGHT}"
        self.root.geometry(self.tkinter_screensize)
    
    def StartMenu(self):
        # Restart screen
        self.root.destroy()
        self.root = tk.Tk()
        self.config_screen()
        startButton = tk.Button(self.root, text="START GAME", 
            font=("Areal, 20"), command=self.MainMenu)
        loadButton = tk.Button(self.root, text="LOAD GAME", 
            font=("Areal, 20"))
        startButton.pack()
        loadButton.pack()
        
    def update_displayLabels(self):
        # Date, Club, Finance
        dateLabel = tk.Label(self.root, text=f"{self.formated_date}\t", 
            font=Fonts.Arial_14)
        clubLabel = tk.Label(self.root, text=f"Club\t", 
            font=Fonts.Arial_14)
        financeLabel = tk.Label(self.root, text=f"Finance", 
            font=Fonts.Arial_14)
        
        dateLabel.grid(row=0, column=0)
        clubLabel.grid(row=0, column=2)
        financeLabel.grid(row=0, column=3)
        
    def MainMenu(self):
        # Restart screen
        self.root.destroy()
        self.root = tk.Tk()
        self.config_screen()
        
        # Menus
        # Proceed week, ViewSquad
        proceedDayButton = tk.Button(self.root, text="PROCEED DAY!",
            font=Fonts.Arial_14, bg='grey', activebackground='grey',
            command=self.ProceedDay)
        ShowSquadButton = tk.Button(self.root, text="SHOW SQUAD",
            font=Fonts.Arial_14, bg='grey', activebackground='grey',
            command=self.ShowSquadMenu)
        # display labels
        self.update_displayLabels()
        
        proceedDayButton.grid(row=1, column=0)
        ShowSquadButton.grid(row=2, column=0)
        
    
    def Run(self):
        self.StartMenu()
        self.root.mainloop()
        
    def ProceedDay(self):
        self.current_date += datetime.timedelta(days=1)
        self.year = self.current_date.year
        self.month = self.current_date.strftime("%b")
        self.day = self.current_date.strftime("%d")
        self.formated_date = f"Date: {self.day} {self.month} {self.year}"
        self.update_displayLabels()
        
    def ShowSquadMenu(self):
        # Restart screen
        self.root.destroy()
        self.root = tk.Tk()
        self.config_screen()
        
        selectedPlayersList = []
        last_index = 0
        
        # for each player set their status and add it to the list the 
        # display player.
        for i, ply in enumerate(self.my_club.players):
            # if player is the last then set last index
            if ply == self.my_club.players[-1]:
                last_index = i
            isSelected = tk.IntVar()    # checkbox status
            player_descr = f"""
{ply.name}     {ply.pos}     {ply.avg}
            """
            playerCheckbox = tk.Checkbutton(self.root, text=player_descr,
                variable=isSelected, onvalue=1, offvalue=0,
                font=Fonts.Arial_14)
            selectedPlayersList.append(isSelected)
            playerCheckbox.grid(row=i)
            
        ConfirmSquadButton = tk.Button(self.root, text="Submit!",
            command= self.confirm_startingLineup)
        ConfirmSquadButton.grid(row=last_index+1)
        
    def count_selectedPlayers(self, selectedPlayersList):
        """selectionlist: [1, 0, 0, 1, 0] count number of 1's"""
        valuesum = [x for x in selectedPlayersList if x == 1]
        return len(valuesum)
    
    def confirm_startingLineup(self, selectedPlayersList, maxsize=4):
        playersSelected = [x.get() for x in selectedPlayersList]
        number_of_selected_players = self.count_selectedPlayers(playersSelected)
        if number_of_selected_players >= 4:
            for i, x in enumerate(selectionlist):
                if x:
                    self.my_starting_lineup.append(self.my_club.players[i])
        else:
            messagebox.showwarning("Incomplete starting lineup",
                f"Starting lineup must be {maxsize} players. NOT {number_of_selected_players}")


SoccerSim = Game((700, 500))
SoccerSim.Run()



# UPDATES
# 1. SHOW SQUAD IS DONE NOW ALLOW UP TO 4 PLAYERS TO BE SELECTED AND SET
#    AS STARTING LINEUP
# 2. ADD COMPETITION MENU AND TRY TO USE THE TABULATE LIBRAEY TO DRAW
#    A TABLE
# 3. SEPARATE STUFF USING FRAMES..
