import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def battle(self, opponent):
        winner = random.choice([self.name, opponent.name])
        print(f"Winner: {winner}")