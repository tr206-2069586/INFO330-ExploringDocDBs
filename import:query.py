import sqlite3  
import sys      
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

print()
print("Pokemon named Pikachu")
print("----------------------------------------------")
pokemonPika = pokemonColl.find({"name": "Pikachu"})
for pikachu in pokemonPika:
    print(pikachu['name'])

print()
print("Pokemon with more then 150 attack")
print("----------------------------------------------")
highAttack = pokemonColl.find({"attack": { "$gt" : 150 }})
for highAttackName in highAttack:
    print(highAttackName['name'])

print()
print("Pokemon that have the ability overgrow!")
print("----------------------------------------------")
overgrowAbility = pokemonColl.find({"abilities": {"$regex" : "Overgrow"}})
for overgrowAbilityName in overgrowAbility:
    print(overgrowAbilityName['name'])