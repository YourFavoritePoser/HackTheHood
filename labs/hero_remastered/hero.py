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

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        effective_damage = damage - self.defend()
        if effective_damage < 0:
            effective_damage = 0
        self.current_health -= effective_damage
        if self.current_health < 0:
            self.current_health = 0

    def battle(self, opponent):
        if not self.abilities and not opponent.abilities:
            print("Draw")
            return

        while self.current_health > 0 and opponent.current_health > 0:
            # Heroes turn
            damage_to_opponent = self.attack()
            opponent.take_damage(damage_to_opponent)
            print(f"{self.name} attacks {opponent.name} for {damage_to_opponent} damage.")
            print(f"{opponent.name}'s health: {opponent.current_health}")
            
            if opponent.current_health <= 0:
                print(f"{self.name} won!")
                return

            # Opponents turn
            damage_to_self = opponent.attack()
            self.take_damage(damage_to_self)
            print(f"{opponent.name} attacks {self.name} for {damage_to_self} damage.")
            print(f"{self.name}'s health: {self.current_health}")
            
            if self.current_health <= 0:
                print(f"{opponent.name} won!")
                return
