from hero import Hero
import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.living_heroes = []
        self.kills = 0
        self.deaths = 0

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero):
        self.heroes.remove(hero)

    def view_all_heroes(self):
        for h in self.heroes:
            print(f"- {h.name}")

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1

    def update_living_heroes(self):
        self.living_heroes = [hero for hero in self.heroes if hero.is_alive()]

    def team_battle(self, opponent_team):
        self.update_living_heroes()
        opponent_team.update_living_heroes()        

        chosen_hero = random.choice(self.heroes)
        chosen_opponent = random.choice(opponent_team.heroes)
        
        while self.living_heroes and opponent_team.living_heroes:
            chosen_hero = random.choice(self.living_heroes)
            chosen_opponent = random.choice(opponent_team.living_heroes)

            print(f"{chosen_hero.name} is fighting {chosen_opponent.name}")
            chosen_hero.battle(chosen_opponent)

        if chosen_hero.is_dead():
            self.heroes.remove(chosen_hero)
            self.add_death()
            opponent_team.add_kill()

        elif chosen_opponent.is_dead():
            opponent_team.heroes.remove(chosen_opponent)
            opponent_team.add_death()
            self.add_kill()
