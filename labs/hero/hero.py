import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors = []
        self.abilities = []

    def battle(self, opponent):
        self.opponent = opponent
        self.winner = random.choice([self.name, self.opponent])
        return self.winner
    
    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += Ability.attack()
        return total_damage
    
    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_defence += Armor.block()
        return total_block
    
    def take_damage(self, damage):
        self.damage = damage
    
if __name__ == "__main__":
    hero = Hero("Stink")
    ability = Ability

    punch = Ability("Punch", 30)
    kick = Ability("Kick", 40)
    stab = Ability("Stab", 80)
    grenade = Ability("Grenade", 100)

    bulletproof_vest = Armor("Bulletproof Vest", 60)

    hero.add_ability(punch)
    hero.add_ability(kick)
    hero.add_ability(stab)
    hero.add_ability(grenade)

    print(f"{hero.name}'s abilities: ")
    for ability in hero.abilities:
        print(f"- {ability.name} with max damage of {ability.max_damage}")