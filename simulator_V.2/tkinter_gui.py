import tkinter
from tkinter import *

class Game:
    def __init__(self, title: str, screen_size: tuple, bg: str):
        self.title = title
        self.screen_size = screen_size
        self.bg = bg
        self.root = tkinter.Tk()
        self.RedefineWindow()
        self.root.mainloop()

    def RedefineWindow(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry(f"{self.screen_size[0]}x{self.screen_size[1]}")
        self.root.config(background=self.bg)

    def Start(self):
        self.RedefineWindow()
        TitleLabel = tk.Label(master=self.root, text=self.title.upper(), width=30, font=("comicsans", 30))
        StartButton = tk.Button(master=self.root, text="START GAME", width=20, font=("Areal", 30), command=self.StartGame)
        LoadButton = tk.Button(master=self.root, text="LOAD GAME", width=20, font=("Areal", 30))

        TitleLabel.pack(pady=40)
        StartButton.pack(pady=60)
        LoadButton.pack()
        self.mainloop()

    def StartGame(self):
        self.RedefineWindow()
        self.mainloop()

    def mainloop(self):
        self.root.mainloop()

# game = Game("Soccer-Simulator 23", (500, 700), "grey")
# game.Start()

tk_root  = Tk()

tk_root.mainloop()


