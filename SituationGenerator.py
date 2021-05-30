import numpy as np
import monsters

dungeon_encounters = ['hostile_monster', 'friendly_monster', 'treasure']

ability_checks = ['trap', 'hidden_key', 'hidden_passage', 'hidden_treasure']

town_encounters = ['royal', 'holiday', 'oracle', 'brawl_fight', 'sale', 'monster_attack']

travel_encounters = ['merchant', 'hunters', 'animal', 'monster', 'travelers']

def get_monster_attributes(monster):
    data = monster.to_numpy()
    data.reshape(1, 20)

    return data



def gen_monster_encounter(level):
    light_level = 'normal'
    encounter1 = None
    encounter2 = None
    encounter3 = None
    encounters = list()
    monster_encounters = list()

    ran = np.random.randint(1, 100)
    if ran >= 0:
        encounter1 = np.random.choice(dungeon_encounters)
        encounters.append(encounter1)
    if ran >= 70:
        encounter2 = np.random.choice(dungeon_encounters)
        encounters.append(encounter2)
    if ran >= 90:
        encounter3 = np.random.choice(dungeon_encounters)
        encounters.append(encounter3)
    
    ability_check1 = ''
    ability_check2 = ''

    ran2 = np.random.randint(1, 100)
    if ran2 >= 70:
        ability_check1 = np.random.choice(ability_checks)
        ability_checks.append(ability_check1)
    if ran2 >= 90:
        ability_check2 = np.random.choice(ability_checks)
        ability_checks.append(ability_check2)

    if encounter1 and encounter1 == 'hostile_monster':
        monster_encounters.append(monsters.gen_monster(level))
        monster_encounters.append(monsters.gen_monster(level))
    if encounter2 and encounter2 == 'hostile_monster':
        monster_encounters.append(monsters.gen_monster(level))
        monster_encounters.append(monsters.gen_monster(level))
    
        
    

gen_monster_encounter(1)

while True:
    print('Hi, welcome to D&D Generator for Dungeon Masters')
    print('Simple type an option to begin...')
    print('Gen monster, Gen loot, Gen ability checks\n')
    answer = input('What would you like to do Dungeon Master?')

    if answer.lower == 'quit':
        break





