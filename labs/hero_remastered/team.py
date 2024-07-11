from hero import Hero
import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.kills = 0
        self.deaths = 0

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero):
        self.heroes.remove(hero)

    def view_all_heroes(self):
        for h in self.heroes:
            print(f"- {h.name}")

    def attack(self, opponent_team):
        living_heroes = []
        living_opponents = []

        while living_heroes and living_opponents:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            print(f"{hero.name} is fighting {opponent.name}")
            hero.battle(opponent)

            living_heroes = [hero for hero in self.heroes if hero.is_alive()]
            living_opponents = [hero for hero in opponent_team.heroes if hero.is_alive()]

        if living_heroes:
            print(f"{self.name} won the battle!")
        else:
            print(f"{opponent_team.name} won the battle!")            
