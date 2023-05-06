import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

# Modified battle outcome so now it's a weighted outcome based on who has more advantages
def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])
    p1 = 0
    p2 = 0
    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            p1 += 1
            print(pokemon1['name'] + " has the advantage in " + stat)
        elif pokemon2[stat] > pokemon1[stat]:
            p2 += 1
            print(pokemon2['name'] + "'s " + stat + " is superior")
    p1WinChange = (float(p1/6) * 100)
    p2WinChange = (float(p2/6) * 100)
    winner = random.choices([0,1], weights=(p1WinChange,p2WinChange), k=1)
    if winner[0] == 0: print("Battle results: " + pokemon1['name'])
    if winner[0] == 1: print("Battle results: " + pokemon2['name'])

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
