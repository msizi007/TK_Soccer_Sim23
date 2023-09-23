from abc import ABC, abstractmethod

class Fonts(ABC):
    def __init__(self):
        super().__init__()

    @staticmethod
    def Arial_14(self):
        return "Arial, 14"
    
class Colors(ABC):
    def __init__(self):
        super().__init__()
       
    @staticmethod 
    def Black(self):
        return "#000000"
    @staticmethod
    def Green(self):
        return '#269538'
    @staticmethod
    def Yellow(self):
        return 'yellow'
    def Blue(self):
        return "Blue"