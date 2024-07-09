import random

class Weapon:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        self.damage = random.randint(0, max_damage)

    def attack(self):
        return self.damage
