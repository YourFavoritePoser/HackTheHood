class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.kills = 0
        self.deaths = 0

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero):
        self.heroes.remove(hero)

    def view_all_heroes(self):
        for h in self.heroes:
            print(f"- {h.name}")
