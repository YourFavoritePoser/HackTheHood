import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.team_kills = 0
        self.team_deaths = 0

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero):
        self.heroes.remove(hero)

    def add_team_kill(self):
        self.team_kills += 1
        return self.team_kills
    
    def add_team_death(self):
        self.team_deaths += 1
        return self.team_deaths
    
    def team_attack(self, opponent):
        living_heroes = self.heroes[:]
        living_opponents = opponent.heroes[:]
