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

    '''def battle(self, opponent):
        winner = random.choice([self.name, opponent.name])
        print(f"Winner: {winner}")'''

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self, opponent):
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def defend(self):
        total_block = 0

        for armor in self.armors:
            total_block += armor.block()

        return total_block
    
    def take_damage(self, opponent):
        effective_damage = self.attack() - self.defend()
        if effective_damage < 0:
            effective_damage = 0
            
        opponent.current_health -= effective_damage