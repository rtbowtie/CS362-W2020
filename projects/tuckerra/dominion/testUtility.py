
import Dominion
import random
from collections import defaultdict

#setting the number of Victory Cards based on whether the number of players passes a breakpoint amount
def numVictory(numPlayers, breakpoint):
    if numPlayers>breakpoint:
        return 12
    else:
        return 8

#setting the number of curses cards based on the number of players
def numCurses(numPlayers):
    return -10 + 10 * numPlayers

#setting up the box of all cards, including the number of gardens cards based on the number of Victory cards
#argument passed in
def GetBoxes(nV):
    #Define box
    box = {}
    box["Woodcutter"]=[Dominion.Woodcutter()]*10
    box["Smithy"]=[Dominion.Smithy()]*10
    box["Laboratory"]=[Dominion.Laboratory()]*10
    box["Village"]=[Dominion.Village()]*10
    box["Festival"]=[Dominion.Festival()]*10
    box["Market"]=[Dominion.Market()]*10
    box["Chancellor"]=[Dominion.Chancellor()]*10
    box["Workshop"]=[Dominion.Workshop()]*10
    box["Moneylender"]=[Dominion.Moneylender()]*10
    box["Chapel"]=[Dominion.Chapel()]*10
    box["Cellar"]=[Dominion.Cellar()]*10
    box["Remodel"]=[Dominion.Remodel()]*10
    box["Adventurer"]=[Dominion.Adventurer()]*10
    box["Feast"]=[Dominion.Feast()]*10
    box["Mine"]=[Dominion.Mine()]*10
    box["Library"]=[Dominion.Library()]*10
    box["Gardens"]=[Dominion.Gardens()]*nV
    box["Moat"]=[Dominion.Moat()]*10
    box["Council Room"]=[Dominion.Council_Room()]*10
    box["Witch"]=[Dominion.Witch()]*10
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
    box["Militia"]=[Dominion.Militia()]*10
    box["Spy"]=[Dominion.Spy()]*10
    box["Thief"]=[Dominion.Thief()]*10
    box["Throne Room"]=[Dominion.Throne_Room()]*10
    return box

#returning a specified number of random cards from the box
def randomCards(box, val):
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:val]
    return defaultdict(list,[(k,box[k]) for k in random10])

#adding a standard number of particular cards to the supply provided as an argument
#using the number of players, the calculated number of victory and curse cards
def addStandardToSupply(supply, nV, nC, playerNum):
    supply["Copper"]=[Dominion.Copper()]*(60-playerNum*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*nV
    supply["Duchy"]=[Dominion.Duchy()]*nV
    supply["Province"]=[Dominion.Province()]*nV
    supply["Curse"]=[Dominion.Curse()]*nC
