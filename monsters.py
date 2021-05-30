from typing import Sized
import pandas
import numpy as np

class Monster: 
    def __init__(self, name, size, type, align, AC, HP, speeds, STR, DEX, CON, INT, WIS, CHA,
     savingThrows, skills, WRI, senses, languages, CR, add):
        self.name = name
        self.size = size 
        self.type = type
        self.align = align
        self.AC = AC
        self.HP = HP
        self.speeds = speeds
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        self.savingThrows = savingThrows
        self.skills = skills
        self.WRI = WRI
        self.senses = senses
        self.languages = languages
        self.CR = CR
        self.add = add
    def printATRS(self):
        return 'Name: {0} Type: {1} Challenge Rating: {2} Size: {3} Align: {4}\nSTATS\nHealth: {5} Armor Class: {6}\nSTR {7} DEX {8} CON {9}\nINT {10} WIS {11} CHA {12}\nSkills: {13} Senses: {14}\nWeaknesses and Resistances: {15} Saving Throws: {16} Languages: {17}\nAdditional info: {18}\n'.format(self.name, 
        self.type, self.CR, self.size, self.align, self.HP, self.AC,
        self.STR, self.DEX, self.CON, self.INT, self.WIS, self.CHA, self.skills, self.senses,
        self.WRI, self.savingThrows, self.languages, self.add)
        

monsters = pandas.read_csv('monsters.csv')

easyMonsters = monsters[monsters['CR'].astype(float) < 5]
mediumMonsters = list()
hardMonsters = list()
resistances = ['acid', 'bludgeoning', 'cold', 'fire', 'force', 'lightning',
'necrotic', 'piercing', 'poison', 'physic', 'radiant', 'slashing', 'thunder']
weaknesses = [['acid', 'bludgeoning', 'cold', 'fire', 'force', 'lightning',
'necrotic', 'piercing', 'poison', 'physic', 'radiant', 'slashing', 'thunder']]

def gen_monster(level):
    monster = monsters[monsters['CR'].astype(float) <= level]
    data = monster.sample(n=1)
    data = data.to_numpy()
    data.reshape(1, 20)
    monster1 = Monster(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4],
    data[0][5], data[0][6], data[0][7], data[0][8], data[0][9], data[0][10], data[0][11], data[0][12], data[0][13], data[0][14],
    data[0][15], data[0][16], data[0][17], data[0][18], data[0][19])
    
    return monster1      
