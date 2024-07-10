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

print(f"{toad.name}'s Abilities:")
for ability in toad.abilities:
    print(f"- {ability.name} max damage: {ability.max_damage}")
print(f"HP: {toad.current_health}")

print(f"{scooby.name}'scoobys Armors:")
for armor in scooby.armors:
    print(f"- {armor.name} max block: {armor.max_block}")
print(f"HP: {scooby.current_health}")


# Attack
toad.attack(scooby)

print(scooby.current_health)