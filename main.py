import os
import csv
import __init__ as init
import random
import numpy as np

# restrict forbidden pairings

# generate array of players
players = init.extractPlayers()

# print teams and averages


# teams = []
# for i in range (0,11):


# choose 4 random players
TeamsArray = []
teamSample1 = []
teamSampleAvg = 0
teamSample1 = random.sample(players, init.teamSize) # choosing X random players

for samplePlayer in teamSample1:
    teamSampleAvg = teamSampleAvg + samplePlayer.playerRating

teamSampleAvg = teamSampleAvg/len(teamSample1)

TeamsArray.append(init.Team(1, teamSample1, teamSampleAvg))

# remove them from the list of players to randomly choose from
remainingPlayers = init.extractPlayers()
remainingPlayers = [player for player in remainingPlayers if player.id not in {p.id for p in teamSample1}] # FOR KIRK - list comprehension


#finish selecting the teams
teamSample2 = random.sample(remainingPlayers, init.teamSize) # choosing X random players
teamSampleAvg = 0
for samplePlayer in teamSample2:
    teamSampleAvg = teamSampleAvg + samplePlayer.playerRating

teamSampleAvg = teamSampleAvg/len(teamSample2)

TeamsArray.append(init.Team(2, teamSample2, teamSampleAvg))


# debugging
for team in TeamsArray:
    print(vars(team))
    for player in team.players:
        print("Team #"+ str(team.teamId) + ": " + str(vars(player)))

# for players in teamSample1:
#     print (vars(players))

# print(len(teamSample1))
# print(len(teamSample2))