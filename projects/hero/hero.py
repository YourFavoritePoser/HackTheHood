class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.weapons = []
        self.armor = []
        self.kills = 0
        self.deaths = 0

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def attack(self):
        total_damage = 0
        for weapon in self.weapons:
            total_damage += weapon.attack()
        return total_damage
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_dead(self):
        return self.health == 0
    
    def battle(self):
        pass
    
    def add_kill(self):
        self.kills += 1
        return self.kills
    
    def add_death(self):
        self.deaths += 1
        return self.deaths
