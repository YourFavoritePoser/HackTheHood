from hero import Hero
from ability import Ability

# Heroes
toad = Hero("Toad")
scooby = Hero("Scooby-Doo")

print(toad.name)
print(toad.current_health)

print("--------------------------")

print(scooby.name)
print(scooby.current_health)

print("--------------------------")

# Abilities
fart = Ability("Fart", 35)
bite = Ability("Bite", 40)

# Battle
toad.battle(scooby)

# testing attributes
print(fart.attack())