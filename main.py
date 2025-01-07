import os
import csv
import __init__ as init
import random

# restrict forbidden pairings

# generate array of players
players = init.extractPlayers()

team1 = []

team1 = random.sample(players,4)

for i in range(0,4):
    print(str(i) + " " + team1[i].name)