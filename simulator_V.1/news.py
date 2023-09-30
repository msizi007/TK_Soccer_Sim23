"Imports"
from random import choice

class News:
    "Class for telling and tracking latest news"
    def __init__(self):
        pass

    def new_manager_assigned(self, manager_name: str, club_name: str):
        "gives a report that the manager has been assigned as a new manager"
        news = [f"{manager_name} has been assigned as the new manager at {club_name}! Some fans are quite dissapointed",
                f"{club_name} has decided to take {manager_name} as their new manager. Fans looking forward to {manager_name}'s perfomance",
                f"fans demand had been met and {club_name} has sacked the old manager and hired {manager_name} as their new manager!"]
        return choice(news)

    def manager_sacked(self, manager_name: str, club_name: str):
        "gives a report that a certain club has sacked the manager"
        news = [f"{manager_name} has been sacked by {club_name}. The club seemed not satisfied with his perfomance and finally took a decision",
                f"{manager_name} says after all he has done for the team they decided to fire him. {club_name} might regret this decision."]
        return choice(news)