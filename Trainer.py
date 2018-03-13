'''
Created on Mar 11, 2018
To Dos:
Implement Health and battle schemes
Implement map and encounter and catch rates
Implement item usage
Implement Healing
Implement PvP
Implement Gender + Breeding
Implement GYMS + STORY
Implement ability and attack effects + STATUS
@author: Jason Huang SBU Class of 2021
'''
from api import reqData, reqMoveData
import random
try: items = iteritems
except NameError: pass
try: input = raw_input
except NameError: pass

class Trainer(object):
    ''' name = ""
    pokeBox = [] #pokeBox Library
    party = [] #party library
    caughtSpecies = [] #Pokedex library
    dexCount = 0; #Dex library
    money = 0;
    items = []  # Holds all items in the trainer. Acts as 'bag'
    currentLoc = 1  # Starting Location default to 1 for noobs
    bagSize = 0
    partyLimit = 0
    '''
    def __init__(self, name):
        self.trainerDat = {'name': '', 'pokeBox': [] , 'party' :[], 'caughtSpecies' : [], 'dexCount' : 0, 'money' : 0, 'items': [], 'currentLoc' : 1, 'bagSize' : 0, 'partyLimit' : 0}
        self.trainerDat['name'] = name
        self.trainerDat['money'] += 500
        self.trainerDat['bagSize'] = 100
        self.trainerDat['partyLimit'] = 6
       
    def earn(self, amt):
        self.trainerDat['money'] += amt;
       
    def spend(self, amt):
        self.trainerDat['money'] -= amt;
        
    def catchPoke(self, poke):
        caught = False
        for x in range(0, len(self.trainerDat['caughtSpecies'])):
            if poke.getPokemon()["name"] == self.trainerDat['caughtSpecies'][x]:
                caught = True
        
        if not caught:
            self.trainerDat['caughtSpecies'].append(poke.getPokemon()["name"])
            self.trainerDat['dexCount'] += 1
        if len(self.trainerDat['party']) >= self.trainerDat['partyLimit'] :
            self.trainerDat['pokeBox'].append(poke)
        else:
            self.trainerDat['party'].append(poke)
        
            
    def getItem(self, item):
        if self.trainerDat['bagSize'] <= len(self.items):
            print('\nBag is full')
        else:
            self.trainerDat['items'].append(item)
    
    def tossItem(self, item):
        for x in self.trainerDat['items']:
            if x["name"] == item["name"]:
                self.items.remove(item)
            else:
                print('\nThe item you are trying to toss does not exist')
    
    #Mutators
    
    def addToLoc(self, num):    
        self.trainerDat['currentLoc'] += num
        
    def addToPartyLimit(self, num):
        self.trainerDat['partyLimit'] += num
        
    def addToBagSize(self, num):
        self.trainerDat['bagSize'] += num
        
    def depositPoke(self, index):
        if index > len(self.trainerDat['party']):
            print('\nThe pokemon at the index does not exist')
        self.trainerDat['pokeBox'].append(self.trainerDat['party'].pop(index))
    def setTrainerData(self, data):
        self.trainerDat = data
        
    def getTrainerData(self):
        return self.trainerDat
    
    def getName(self):
        return self.trainerDat['name']
    
    def printParty(self):
        s = ""
        for x in range(len(self.trainerDat['party'])) :
            s += "\n" + str(x + 1) + ")" + self.trainerDat['party'][x].toString()
        return s
    
    def printBox(self):
        s = ""
        for x in range(len(self.trainerDat['pokeBox']) ) :
            s += "\n" + str(x + 1) + ")" + self.trainerDat['pokeBox'][x].toString()
        return s
    
    def toString(self):
        st = "\nName:" + self.trainerDat['name'] + "\nParty:" + self.printParty() + "\nMoney:" + str(self.trainerDat['money']) + "\nCurrent Location:" + str(self.trainerDat['currentLoc']) + "\nDex Count:" + str(self.trainerDat['dexCount']) + "\nPokemon PC: " + self.printBox()
        return st
    
    
class Pokemon(object):
    
    def __init__(self, data, level):
        self.pokeDat = {'statBoosters': [1,1,1,1,1,1], 'stats': [10,10,10,10,10,10], 'Health': 100, 'moveLimit': 4, 'exp': 1000, 'owner': "", 'shiny': False, 'level' : 1, 'data' : '', 'nature' : '', 'nickName' : '', 'ev' : [0,0,0,0,0,0], 'iv' : [1,1,1,1,1,1], 'ability' : '', 'gender' : 'genderless', 'moves': [] }
        if 999 <= random.randint(0,1000):
            self.pokeDat['shiny'] = True
        self.pokeDat['data'] = data
        self.pokeDat['data']["moves"] = sorted(data["moves"], key = lambda k: k["version_group_details"][0]["level_learned_at"]) #Sorting the moves by level
        self.pokeDat['nature'] = reqData("nature/" + str(random.randint(1,20)))
        self.pokeDat['level'] = level
        self.pokeDat['exp'] = level * 1000
        self.pokeDat['nickName'] = data['name'].upper()
        if 90 >= random.randint(0,100):
            for x in range(0,6):
                self.pokeDat['iv'][x] = random.randint(0,31)
        else:
            for x in range(0,6):
                self.pokeDat['iv'][x] = random.randint(28,31)
                
        if 80 <= random.randint(0,100) or len(data["abilities"]) == 1:
            self.pokeDat['ability'] = reqMoveData(data["abilities"][0]["ability"]["url"])
        else:
            if len(data["abilities"]) > 2:
                self.pokeDat['ability'] = reqMoveData(data["abilities"][random.randint(1,2)]["ability"]["url"])
            else:
                self.pokeDat['ability'] = reqMoveData(data["abilities"][1]["ability"]["url"])

    def increEv(self, index, amt): 
        if not self.pokeDat['ev'][index] >= 252:
            self.pokeDat['ev'][index] += amt
    
    def setOwner(self, name):
        self.pokeDat['owner'] = name
    
    def getStatBoosters(self):
        return self.pokeDat['statBoosters']
    
    def setStatBoosters(self, array):
        self.pokeDat['statBoosters'] = array
    
    def levelUp(self):
        self.pokeDat['level'] += 1
        for x in range(0, len(self.pokeDat['data']["moves"])):
            y = self.pokeDat['data']["moves"][x]
            if y["version_group_details"][0]["move_learn_method"]["name"] == "level-up" :
                if y["version_group_details"][0]["level_learned_at"] == self.pokeDat['level'] :
                    print("\nYour pokemon can learn the new move " + y["move"]["name"] + ".")
                    confidenceRating = True
                    while confidenceRating : 
                        truth = input("\nDo you want to learn this new move? (Y/N)")
                        confidence = input("\nAre you sure? (Y/N)")
                        if confidence == "Y" :
                            confidenceRating = False
                        if confidence == "N" :
                            continue
                        else: 
                            print("Choose a valid response. (Y/N)")
                    if truth == "Y":
                        if len(self.pokeDat['moves']) >= self.pokeDat['moveLimit']:
                            index = input("\nWhich existing move do you want to replace?:")
                            for x in range(self.pokeDat['moveLimit']):
                                print("\n(" + str(x) + ")" + self.pokeDat['moves'][x].toString())
                            while index < 1 or index > len(self.pokeDat['moves'] - 1) :
                                print("\nChoose a valid response.")
                                index = input(self.pokeDat["moves"])
                            self.pokeDat['moves'][index - 1] = Moves(reqMoveData(y["move"]["url"]))
                        else: 
                            self.pokeDat['moves'].append(Moves(reqMoveData(y["move"]["url"])))
                if y["version_group_details"][0]["level_learned_at"] > self.pokeDat['level'] :
                    break
        
    def getPokemon(self):
        return self.pokeDat['data']

    def getMoves(self):
        index = []
        y = self.pokeDat['data']["moves"]
        for x in range(len(y)) :
            if y[x]["version_group_details"][0]["move_learn_method"]["name"] == "level-up" :
                if y[x]["version_group_details"][0]["level_learned_at"] > self.pokeDat['level'] :
                    break;
                index.append(x)
         
    
        while not (len(self.pokeDat['moves']) >= self.pokeDat['moveLimit'] or len(index) == 0) :
            self.pokeDat['moves'].append(Moves(reqMoveData(y[index.pop()]["move"]["url"]))) 
            
    def increMoveLimit(self,amt):
        self.pokeDat['moveLimit'] += amt
        
    def increExp(self, amt):
        if not self.pokeDat['exp'] >= 100000 :
            self.pokeDat['exp'] += amt
            while (self.pokeDat['exp'] - self.pokeDat['level'] * 1000) >= 1000 :
                self.levelUp()
        
    def getData(self):
        return self.pokeDat
    def setData(self, data):
        self.pokeDat = data 
    
    def toString(self):
        s = "\nName:" + self.pokeDat['nickName']
        s += "\nLevel:" + str(self.pokeDat['level'])
        s += "\nNature:" + str(self.pokeDat['nature']["name"]).upper()
        s += "\nAbility:" + str(self.pokeDat['ability']["name"]).upper()
        s += "\nMoves:"
        for x in range(len(self.pokeDat['moves'])):
            s += "\n(" + str(x+1) + ")" + self.pokeDat['moves'][x].toString()
        return s
    
class Moves(object):
    
    def __init__(self, data):
        self.movedat = {'effect' : "" , 'priority':0, 'critChance': 10, 'data' : {}, 'pp': 0, 'name': "", 'power': 0, 'accuracy' : 0, 'effectChance' : 0}
        self.movedat['name'] = data["name"].upper()
        self.movedat['data'] = data
        self.movedat['pp'] = data["pp"]
        self.movedat['power'] = data["power"]
        self.movedat['accuracy'] = data["accuracy"]
        self.movedat['effectChance'] = data["effect_chance"]
        self.movedat['effect'] = data["effect_entries"][0]["short_effect"] #When implementing battle, use reg effect
        self.movedat['priority'] = data["priority"]
    
    def setCritChance(self, value) :
        self.movedat['critChance'] = value
        
    def decreasePP(self, amt):
        self.movedat['pp'] -= amt
    
    def getPower(self):
        return self.movedat['power']
    
    def getAccuracy(self):
        return self.movedat['accuracy']
    
    def getPriority(self):
        return self.movedat['priority']
    
    def toString(self):
        s = "\n" + self.movedat['name'] + "\tAccuracy:" + str(self.movedat['accuracy']) 
        s += "\tPP:" + str(self.movedat['pp']) + "\tPower:" + str(self.movedat['power'])
        s += "\n" + self.movedat['effect'] +"\n"
        return s