from hero import Hero
from ability import Ability
from armor import Armor

# Create heroes
toad = Hero("Toad")
scooby = Hero("Scooby-Doo")

# Create abilities and armors
blow = Ability("Blow", 70)
bite = Ability("Bite", 80)
shield = Armor("Shield", 30)
helmet = Armor("Helmet", 20)

# Assign abilities and armors to heroes
toad.add_ability(blow)
toad.add_armor(shield)
scooby.add_ability(bite)
scooby.add_armor(helmet)

# Start battle
scooby.battle(toad)
