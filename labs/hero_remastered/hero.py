from ability import Ability
from armor import Armor
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.weapons = []
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1

    def attack(self):
        total_damage = sum(a.attack() for a in self.abilities)
        return total_damage

    def defend(self):
        total_block = sum(b.block() for b in self.armors)
        return total_block

    def take_damage(self, damage):
        effective_damage = max(damage - self.defend(), 0)
        self.current_health -= effective_damage
        self.current_health = max(self.current_health, 0)

    def is_alive(self):
        return self.current_health > 0

    def battle(self, opponent):
        print(f"{self.name} battles {opponent.name}")
        while self.is_alive() and opponent.is_alive():
            # Heroes Turn
            print(f"{self.name}'s Turn:")
            opponent.take_damage(self.attack())
            # Opponents Turn
            print(f"{opponent.name}'s Turn:")
            self.take_damage(opponent.attack())

        winner = self if self.is_alive() else opponent
        print(f"The Winner is {winner.name}!")

