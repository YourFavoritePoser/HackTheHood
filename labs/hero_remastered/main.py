from hero import Hero
from ability import Ability
from armor import Armor

# Heroes
toad = Hero("Toad")
scooby = Hero("Scooby-Doo")

# Abilities
blow = Ability("Blow", 30)
bite = Ability("Bite", 35)

# Armors
shield = Armor("Shield", 30)
helmet = Armor("Helmet", 20)

# Toads armors and abilities
toad.add_ability(blow)
toad.add_armor(shield)

# Scoobys armors and abilities
scooby.add_ability(bite)
scooby.add_armor(helmet)

# Print
print(f"{toad.name}'s Abilities: ")
for ability in toad.abilities:
    print(f"- {ability.name}")

print(f"{toad.name}'s Armors: ")
for armor in toad.armors:
    print(f"- {armor.name}")