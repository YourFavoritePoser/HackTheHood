from hero import Hero

toad = Hero("Toad")
scooby = Hero("Scooby-Doo")

print(toad.name)
print(toad.current_health)

print("--------------------------")

print(scooby.name)
print(scooby.current_health)

print("--------------------------")

toad.battle(scooby)