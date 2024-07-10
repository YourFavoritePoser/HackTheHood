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

print(f"{toad.name}'s Abilities:")
for a in toad.abilities:
    print(f"- {a.name} with max damage of {a.max_damage}")

print(f"{toad.name}'s Armors:")
for a in toad.armors:
    print(f"- {a.name} with max block of {a.max_block}")

print(f"HP: {toad.current_health}")

print("------------------------")

# Scoobys armors and abilities
scooby.add_ability(bite)
scooby.add_armor(helmet)

print(f"{scooby.name}'s Abilities:")
for a in scooby.abilities:
    print(f"- {a.name} with max damage of {a.max_damage}")

print(f"{scooby.name}'s Armors:")
for a in scooby.armors:
    print(f"- {a.name} with max block of {a.max_block}")

print(f"HP: {scooby.current_health}")

print("------------------------")

# Attack
pass
