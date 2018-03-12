'''
Created on Mar 11, 2018
IMPLEMENTED WITH PYTHON 2.7
@author: Jason
'''

from Trainer import Trainer
from api import getPoke
import random
from Trainer import Pokemon
import pickle

    
def printBreak():
    print("\n----------------------------------------------------")
def continueJourney(trainer):
    q = True
    while(q) :
        print("\nCurrent Journey:")
        print(trainer.toString())
        option = int(raw_input("\nOptions:\n(1)Walk Around\n(2)Next Area\n(3)Shop\n(4)Talk to NPCs\n(5)Poke Center\n(6)PVP\n(7)Save\nMy Choice:"))
        while(not option >=1 or not option <= 7 ):
            option = int(raw_input("\nOptions:\n(1)Walk Around\n(2)Next Area\n(3)Shop\n(4)Talk to NPCs\n(5)Poke Center\n(6)PVP\n(7)Save\nMy Choice:"))
        if(option == 1):
            pokie = Pokemon(getPoke(random.randint(1,802)), random.randint(1,100))
            print("\nA random pokemon spawned: " + pokie.toString())
            print("\nYou caught it!")
            trainer.catchPoke(pokie)
        if(option == 2) :
            trainer.addToLoc(1)
        if(option == 3) :
            print("\nShop is currently not available. Contact Jason for the next update")
        if(option == 4) :
            print("\nThey told you to get a job. You did and earned $500.")
            trainer.earn(500)
        if(option == 5) :
            print("\nThe Poke Center is currently not available. Contact Jason for the next update")
        if(option == 6) :
            print("\nPvP is currently not available. Contact Jason for the next update")
        if(option == 7) :
            pickleSave = open('saveFile.pickle', 'wb')
            pickle.dump(trainer, pickleSave)
            pickleSave.close()
            print("\nSaving and exiting...")
            q = False
def startJourney():
    person = raw_input("\nWelcome to the world of pokemon! I'm professor Oak. WHOMST must you be?")
    choice = int(raw_input("\n" + str(person) +", I'll hand over a starter to you. Choose between Bulbasaur, Squirtle, and Charmander (1,4,7)"))
    starter = Pokemon(getPoke(choice), 5)
    print("\n" + starter.toString() + "\nhas been added to your team!")
    user = Trainer(str(person))
    starter.setOwner(user.getName())
    user.catchPoke(starter)
    continueJourney(user)
printBreak()
print("\nWelcome to Pokemon RPG (ALPHA) By Jason Huang")
printBreak()
try:
    response = int(raw_input("\nDo you want to load a file or start a new adventure (1 for load / 2 for new)"))
    while(not (response == 1 or response == 2)) :
        response = int(raw_input("\nInvalid Response\nDo you want to load a file or start a new adventure (1 for load / 2 for new)"))
    if(response == 1) :
        pickleLoad = open('saveFile.pickle', 'rb')
        trainer = pickle.load(pickleLoad)
        pickleLoad.close()
        continueJourney(trainer)
    else:
        startJourney()
except:
    printBreak()
    print("\nStarting a new adventure!")
    startJourney()
    


