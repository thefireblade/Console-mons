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
from math import floor
try: input = raw_input
except NameError: pass
#Stats are as follows [HP,ATK,DEF,SPA,SPD,SPE]
#BaseStat database is given in reverse order
def calcStats(base, iv, ev, level, nature):
    hp = 0
    atk = 1
    defe = 2
    spa = 3
    spd = 4
    spe = 5
    stat = [0, 0, 0, 0, 0, 0]
    for x in range(5): 
        stat[5-x] = floor((2 * base[x] + iv[5-x] + ev[5-x]) * level / 100 + 5)
    stat[hp] = floor((2 * base[5] + iv[hp] + ev[hp]) * level / 100 + level + 10)
    if(nature == "LONELY") :
        stat[atk] = floor(stat[atk] * 1.1)
        stat[defe] = floor(stat[defe] * .9)
    if(nature == "BRAVE") :
        stat[atk] = floor(stat[atk] * 1.1)
        stat[spe] = floor(stat[spe] * .9)
    if(nature == "ADAMANT") :
        stat[atk] = floor(stat[atk] * 1.1)
        stat[spa] = floor(stat[spa] * .9)
    if(nature == "NAUGHTY"):
        stat[atk] = floor(stat[atk] * 1.1)
        stat[spd] = floor(stat[spd] * .9)
    if(nature == "BOLD") :
        stat[defe] = floor(stat[defe] * 1.1)
        stat[atk] = floor(stat[atk] * .9)
    if(nature == "RELAXED") :
        stat[defe] = floor(stat[defe] * 1.1)
        stat[spe] = floor(stat[spe] * .9)
    if(nature == "IMPISH") :
        stat[defe] = floor(stat[defe] * 1.1)
        stat[spa] = floor(stat[spa] * .9)
    if(nature == "LAX") :
        stat[defe] = floor(stat[defe] * 1.1)
        stat[spd] = floor(stat[spd] * .9)
    if(nature == "TIMID") :
        stat[spe] = floor(stat[spe] * 1.1)
        stat[atk] = floor(stat[atk] * .9)
    if(nature == "HASTY") :
        stat[spe] = floor(stat[spe] * 1.1)
        stat[defe] = floor(stat[defe] * .9)
    if(nature == "JOLLY") :
        stat[spe] = floor(stat[spe] * 1.1)
        stat[spa] = floor(stat[spa] * .9)
    if(nature == "NAIVE") :
        stat[spe] = floor(stat[spe] * 1.1)
        stat[spd] = floor(stat[spd] * .9)
    if(nature == "MODEST") :
        stat[spa] = floor(stat[spa] * 1.1)
        stat[atk] = floor(stat[atk] * .9)
    if(nature == "MILD") :
        stat[spa] = floor(stat[spa] * 1.1)
        stat[defe] = floor(stat[defe] * .9)
    if(nature == "QUIET") :
        stat[spa] = floor(stat[spa] * 1.1)
        stat[spe] = floor(stat[spe] * .9)
    if(nature == "RASH") :
        stat[spa] = floor(stat[spa] * 1.1)
        stat[spd] = floor(stat[spd] * .9)
    if(nature == "CALM") :
        stat[spd] = floor(stat[spd] * 1.1)
        stat[atk] = floor(stat[atk] * .9)
    if(nature == "GENTLE") :
        stat[spd] = floor(stat[spd] * 1.1)
        stat[defe] = floor(stat[defe] * .9)
    if(nature == "SASSY") :
        stat[spd] = floor(stat[spd] * 1.1)
        stat[spe] = floor(stat[spe] * .9)
    if(nature == "CAREFUL") :
        stat[spd] = floor(stat[spd] * 1.1)
        stat[spa] = floor(stat[spa] * .9)
    return stat
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
    
    def getParty(self):
        return self.trainerDat['party']
    
    def getBox(self):
        return self.trainerDat['pokeBox']
    
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
        self.pokeDat = {'base_stats': [0,0,0,0,0,0],'statBoosters': [1,1,1,1,1,1], 'stats': [10,10,10,10,10,10], 'Health': 100, 'moveLimit': 4, 'exp': 1000, 'owner': "", 'shiny': False, 'level' : 1, 'data' : '', 'nature' : '', 'nickName' : '', 'ev' : [0,0,0,0,0,0], 'iv' : [1,1,1,1,1,1], 'ability' : '', 'gender' : 'genderless', 'moves': [] }
        if 999 <= random.randint(0,1000):
            self.pokeDat['shiny'] = True
        self.pokeDat['data'] = data
        self.pokeDat['data']["moves"] = sorted(data["moves"], key = lambda k: k["version_group_details"][0]["level_learned_at"]) #Sorting the moves by level
        self.pokeDat['nature'] = reqData("nature/" + str(random.randint(1,20)))
        self.pokeDat['level'] = level
        for x in range(6):
            self.pokeDat['base_stats'][x] = data["stats"][x]["base_stat"]
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
        self.pokeDat['stats'] = calcStats(self.pokeDat['base_stats'], self.pokeDat['iv'], self.pokeDat['ev'], self.pokeDat['level'], self.pokeDat['nature']["name"])
        
    def increEv(self, index, amt): 
        if not self.pokeDat['ev'][index] >= 252:
            self.pokeDat['ev'][index] += amt
    
    def setOwner(self, name):
        self.pokeDat['owner'] = name
    
    def getStat(self):
        return self.pokeDat['stats']
    
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
    def getAdvancedDetails(self):
        y = self.pokeDat
        s = self.toString()
        s += "\nStats: "
        s += "HP:" + str(y['stats'][0]) + "\tATK:" + str(y['stats'][1]) + "\tDEF:" + str(y['stats'][2])  
        s += "\tSPA:" + str(y['stats'][3]) + "\tSPD:" + str(y['stats'][4]) + "\tSPE:" + str(y['stats'][5])
        s += "\nIVs: "
        s += "HP:" + str(y['iv'][0]) + "\tATK:" + str(y['iv'][1]) + "\tDEF:" + str(y['iv'][2]) 
        s += "\tSPA:" + str(y['iv'][3]) + "\tSPD:" + str(y['iv'][4]) + "\tSPE:" + str(y['iv'][5])
        s += "\nEVs: "
        s += "HP:" + str(y['ev'][0]) + "\tATK:" + str(y['ev'][1]) + "\tDEF:" + str(y['ev'][2]) 
        s += "\tSPA:" + str(y['ev'][3]) + "\tSPD:" + str(y['ev'][4]) + "\tSPE:" + str(y['ev'][5])
        return s;
    
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