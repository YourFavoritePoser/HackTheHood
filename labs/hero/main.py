from hero import Hero
from opponent import Opponent
from weapon import Weapon

import random

if __name__ == "__main__":
    hero = Hero("Dr. Stink")
    opponent = Opponent("Mrs. Stunk")
    
    dagger = Weapon("Dagger", 40)
    sword = Weapon("Sword", 70)

    hero.add_weapon(dagger)
    opponent.add_weapon(sword)

    print(f"{hero.name}'s Weapons:")
    for weapon in hero.weapons:
        print(f"- {weapon.name} with max damage of {weapon.max_damage}")
    print(f"HP: {hero.health}")

    print("------------------------------------------")

    print(f"{opponent.name}'s Weapons:")
    for weapon in opponent.weapons:
        print(f"- {weapon.name} with max damage of {weapon.max_damage}")
    print(f"HP: {opponent.health}")

    print("------------------------------------------")

    while hero.health > 0 and opponent.health > 0:
        print("\nHero's turn:")
        damage = hero.attack()
        opponent.take_damage(damage)
        print(f"{hero.name} attacked {opponent.name} for {random.randint(0, damage)} damage. {opponent.name}'s health is now {opponent.health}.")

        if opponent.is_dead():
            print(f"\n{hero.name} has defeated {opponent.name}!")
            break

        print("\nOpponent's turn:")
        damage = opponent.attack()
        hero.take_damage(damage)
        print(f"{opponent.name} attacked {hero.name} for {random.randint(0, damage)} damage. {hero.name}'s health is now {hero.health}.")

        if hero.is_dead():
            print(f"\n{opponent.name} has defeated {hero.name}!")
            break

    print("\nGame Over")
