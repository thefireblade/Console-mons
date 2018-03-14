'''
Created on Mar 11, 2018
IMPLEMENTED WITH PYTHON 2.7
@author: Jason
'''

from Trainer import Trainer, calcDamageRecieved, whoAttacksFirst
from api import getPoke
import random
from Trainer import Pokemon
import pickle
try: input = raw_input
except NameError: pass
    
def printBreak():
    print("\n----------------------------------------------------")
def continueJourney(trainer):
    q = True
    while(q) :
        print("\nCurrent Journey:")
        print(trainer.toString())
        option = int(input("\nOptions:\n(1)Walk Around\n(2)Next Area\n(3)Shop\n(4)Talk to NPCs\n(5)Poke Center\n(6)PVP\n(7)Save and Exit\nMy Choice:"))
        while(not option >=1 or not option <= 7 ):
            option = int(input("\nOptions:\n(1)Walk Around\n(2)Next Area\n(3)Shop\n(4)Talk to NPCs\n(5)Poke Center\n(6)PVP\n(7)Save and Exit\nMy Choice:"))
        if(option == 1):
            stay = True
            while(stay) :
                option = int(input("\n(1)Catch a random pokemon\n(2)Battle a pokemon in this area\n(3)Leave\nYour choice:"))
                if(option == 1):
                    pokie = Pokemon(getPoke(random.randint(1,802)), random.randint(1,99))
                    print("\nA random pokemon appeared: " + pokie.toString())
                    pokie.obtainMoves()
                    trainer.catchPoke(pokie)
                    print("\nYou caught it!")
                elif(option == 2):
                    alive = 0
                    for x in range(len(trainer.getParty())):
                        if(trainer.getParty()[x].getHealth() > 0) :
                            alive = x
                            break
                    pokie = Pokemon(getPoke(random.randint(1,802)), random.randint(trainer.getParty()[alive].getLevel() - 4, trainer.getParty()[alive].getLevel() + 1))
                    print("\nA random pokemon appeared: " + pokie.toString() + "\n")
                    pokie.obtainMoves()
                    print("\n" + trainer.getParty()[alive].getName() + " was sent out!")
                    current = alive
                    battle = True #TO BE CHANGED LATER, JUST HERE FOR TESTING
                    while(battle):
                            print(trainer.getParty()[current].toString())
                            option = int(input("\n(1)Attack\t(2)Bag\t\t(3)Switch\t(4)Run\nWhat do you want to do?"))
                            if(option == 1):
                                option = int(input("\nAttacking..\t(-1)Go Back\nChoose a move:"))
                                if(option == -1):
                                    pass
                                elif(option >= 1 or option <= len(trainer.getParty()[current].getMoves())) :
                                    randNum = random.randint(1,4) #changes if the person decides to have more than one move
                                    if(whoAttacksFirst(trainer.getParty()[current], pokie)):
                                        print("\n"+ trainer.getParty()[current].getMove(option).getName() +" has been used.")
                                        trainer.getParty()[current].getMove(option).decreasePP(1)
                                        calcDamageRecieved(trainer.getParty()[current], pokie, trainer.getParty()[current].getMove(option))
                                        if(pokie.getHealth() <= 0) :
                                            print("\n" + pokie.getName() + " has fainted.")
                                            trainer.getParty()[current].winBattleExp(pokie)
                                            battle = False
                                            continue
                                        print("\n"+ pokie.getMove(randNum).getName() +" has been used.")
                                        pokie.getMove(randNum).decreasePP(1)
                                        calcDamageRecieved(pokie, trainer.getParty()[current], pokie.getMove(randNum))
                                        if(trainer.getParty()[current].getHealth() <= 0) :
                                            n = -1
                                            for x in range(len(trainer.getParty())) :
                                                if(trainer.getParty()[x].getHealth() > 0):
                                                    n = x
                                            print("\n" + trainer.getParty()[current].getName() + " has fainted.")
                                            if n == -1:
                                                print("All usable pokemon have fainted. You ran from the battle and rushed to the nearest Pokemon Center")
                                                battle = False
                                                stay = False
                                                for x in range(len(trainer.getParty())) :
                                                    trainer.getParty()[x].heal()
                                                continue
                                            else: 
                                                option = int(input("\nChoose another pokemon to fight" + trainer.printParty()))
                                                if(option > len(trainer.getParty()) or option < 0):
                                                    print("\nInvalid choice")
                                                if(trainer.getParty()[option - 1].getHealth() <= 0):
                                                    print("\nInvalid choice, the pokemon selected is fainted and can no longer battle.")
                                                else:
                                                    current = option - 1
                                                    print("\n" + trainer.getParty()[current].getName() + " was sent out!")
                                        print(pokie.toString())
                                    else:
                                        print("\n"+ pokie.getMove(randNum).getName() +" has been used.")
                                        pokie.getMove(randNum).decreasePP(1)
                                        calcDamageRecieved(pokie, trainer.getParty()[current], pokie.getMove(randNum))
                                        if(trainer.getParty()[current].getHealth() <= 0) :
                                            n = -1
                                            for x in range(len(trainer.getParty())) :
                                                if(trainer.getParty()[x].getHealth() > 0):
                                                    n = 1
                                            print("\n" + trainer.getParty()[current].getName() + " has fainted.")
                                            if n == -1:
                                                print("All usable pokemon have fainted. You ran from the battle and rushed to the nearest Pokemon Center")
                                                battle = False
                                                stay = False
                                                for x in range(len(trainer.getParty())) :
                                                    trainer.getParty()[x].heal()
                                                continue
                                            else: 
                                                option = int(input("\nChoose another pokemon to fight" + trainer.printParty()))
                                                if(option > len(trainer.getParty()) or option < 0):
                                                    print("\nInvalid choice")
                                                else:
                                                    if(trainer.getParty()[option - 1].getHealth() <= 0):
                                                        print("\nInvalid choice, the pokemon selected is fainted and can no longer battle.")
                                                    else:
                                                        current = option - 1
                                                        print("\n" + trainer.getParty()[current].getName() + " was sent out!")
                                        print("\n"+ trainer.getParty()[current].getMove(option).getName() +" has been used.")
                                        trainer.getParty()[current].getMove(option).decreasePP(1)
                                        calcDamageRecieved(trainer.getParty()[current], pokie, trainer.getParty()[current].getMove(option))
                                        if(pokie.getHealth() <= 0) :
                                            print("\n" + pokie.getName() + " has fainted.")
                                            trainer.getParty()[current].winBattleExp(pokie)
                                            battle = False
                                            continue
                                        print(pokie.toString())
                                else: 
                                    print("INVALID MOVE, REVERTING..")
                            elif(option == 2):
                                print("\nBag functions do not exist yet, please contact Jason to update")
                            elif(option == 3):
                                print("\nChoose another pokemon to fight" + trainer.printParty())
                                option = int(input("\n(-1)Go Back\nYour Choice:"))
                                if(option == -1):
                                    pass
                                if(option > len(trainer.getParty()) or option < 0):
                                        print("\nInvalid choice")
                                else:
                                    if(trainer.getParty()[option - 1].getHealth() <= 0):
                                        print("\nInvalid choice, the pokemon selected is fainted and can no longer battle.")
                                    else:
                                        current = option - 1
                                        print("\n" + trainer.getParty()[current].getName() + " was sent out!")
                            elif(option == 4):
                                print("You ran away! (Always success in current build)")
                                battle = False
                            else:
                                print("\nInvalid choice")
                elif(option == 3):
                    stay = False
                    continue
                elif(not(option == 1 or option == 2 or option == 3)):
                    print("\nInvalid choice")
                    continue
                print(trainer.toString())
        if(option == 2) :
            trainer.addToLoc(1)
        if(option == 3) :
            print("\nShop is currently not available. Contact Jason for the next update")
        if(option == 4) :
            print("\nThey told you to get a job. You did and earned $500.")
            trainer.earn(500)
        if(option == 5) :
            stay = True
            while(stay) :
                print("\nThe Poke Center is currently not completed. Contact Jason for the next update")
                option = int(input("\nWhat do you want to do?\n(1)View Party\n(2)Heal Party\n(3)Leave"))
                if(option == 1) :
                    for x in range(len(trainer.getParty())):
                        print(trainer.getParty()[x].getAdvancedDetails())
                elif(option == 2):
                    for x in range(len(trainer.getParty())) :
                        trainer.getParty()[x].heal()
                    print("\nYour pokemon party has been healed!")
                elif(option == 3) :
                    print("\nYou decided to leave.")
                    stay = False;
                else:
                    print("\nInvalid choice")
            
        if(option == 6) :
            print("\nPvP is currently not available. Contact Jason for the next update")
        if(option == 7) :
            pickleSave = open('saveFile.pickle', 'wb')
            pickle.dump(trainer, pickleSave)
            pickleSave.close()
            print("\nSaving and exiting...")
            q = False
def startJourney():
    person = input("\nWelcome to the world of pokemon! I'm professor Oak. WHOMST must you be?")
    choice = 2
    while (not(choice == 1 or choice == 4 or choice == 7)):
        choice = int(input("\n" + str(person) +", I'll hand over a starter to you. Choose between Bulbasaur, Squirtle, and Charmander (1,4,7)"))
    starter = Pokemon(getPoke(choice), 5)
    print("\n" + starter.toString() + "\nhas been added to your team!")
    starter.obtainMoves()
    user = Trainer(str(person))
    starter.setOwner(user.getName())
    user.catchPoke(starter)
    continueJourney(user)
printBreak()
print("\nWelcome to Pokemon RPG (ALPHA) By Jason Huang")
printBreak()
try:
    response = int(input("\nDo you want to load a file or start a new adventure (1 for load / 2 for new)"))
    while(not (response == 1 or response == 2)) :
        response = int(input("\nInvalid Response\nDo you want to load a file or start a new adventure (1 for load / 2 for new)"))
    if(response == 1) :
        pickleLoad = open('saveFile.pickle', 'rb')
        trainer = pickle.load(pickleLoad)
        pickleLoad.close()
        continueJourney(trainer)
    else:
        startJourney()
except IOError:
    printBreak()
    print("\nStarting a new adventure!")
    startJourney()
    


