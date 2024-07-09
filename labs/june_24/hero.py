import random as rd

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def battle(self, opponent):
        self.opponent = opponent
        self.opponents = []
        self.winner = f"Winner: {rd.choice(self.opponents)}"
        

Hero("Stink")
Hero.battle("Stunk")


