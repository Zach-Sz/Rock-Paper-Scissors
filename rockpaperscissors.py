# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 16:08:41 2018

@author: Zach
This program fully works. There are no bugs or issues with it
"""

import random

itemtype = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

def playerhand(hand):
    playeroption = True
    playeritem = ''
    while playeroption:
        playeritem = input("(R)ock, (P)aper or (S)cissors").upper()
        if playeritem in ['R', 'P', 'S']:
            playeroutput = itemtype[playeritem]
            return(playeroutput)
        else:
            print("Invalid Choice. Choose a new value")
            
        
def comphand(hand):
    compitem = random.choice('RPS')
    return(compitem)
    
def endgame(game):
    endoption = input("Do you want to (Q)uit? If not, press any other button to continue.").upper()
    if endoption == 'Q':
        endoption = False
        return(endoption)
    else:
        endoption = True
        return(endoption)
    
playerscore = 0
compscore = 0

print("Welcome to Rock, Paper, Scissors")
print("The score is:")
print("Player: " + str(playerscore))
print("Computer: " + str(compscore))

keepplaying = True

while keepplaying:
    print("Make your choice:")
    playeroutput = playerhand(0)
    compoutput = itemtype[comphand(0)]
    print("The computer chose: " + compoutput)
    if playeroutput == 'Rock':
        if compoutput == 'Rock':
            print('Its a draw. No one wins')
        elif compoutput == 'Scissors':
            print('You Win!')
            playerscore = playerscore + 1
        elif compoutput == 'Paper':
            print('You Lose')
            compscore = compscore + 1
    elif playeroutput == 'Paper':
        if compoutput == 'Rock':
            print('You Win!')
            playerscore = playerscore + 1
        elif compoutput == 'Scissors':
            print('You Lose')
            compscore = compscore + 1
        elif compoutput == 'Paper':
            print('Its a draw. No one wins')
    elif playeroutput == 'Scissors':
        if compoutput == 'Rock':
            print('You Lose')
            compscore = compscore + 1
        elif compoutput == 'Scissors':
            print('Its a draw. No one wins')
        elif compoutput == 'Paper':
            print('You Win!')
            playerscore = playerscore + 1
    print("")
    print("The score is:")
    print("Player: " + str(playerscore))
    print("Computer: " + str(compscore))
    print("")
    keepplaying = endgame(0)





