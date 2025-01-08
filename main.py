import os
import csv
import __init__ as init
import random
# import numpy as np

# restrict forbidden pairings

# generate array of players
players = init.extractPlayers()





# calculate the average 
# print teams and averages


# teams = []
# for i in range (0,11):


# choose 4 random players
teamSample = []
teamSample = random.sample(players, init.teamSize) # choosing 4 random players


# remove them from the list of players to randomly choose from
remainingPlayers = init.extractPlayers()

remainingPlayerCount = 0


for remainingPlayer in remainingPlayers:
    teamSamplePlayerCount = 0
    for teamSamplePlayer in teamSample:
        try:
            if remainingPlayers[remainingPlayerCount].id == teamSample[teamSamplePlayerCount].id:
                print(remainingPlayers[remainingPlayerCount].name + " " + teamSample[teamSamplePlayerCount].name)
                print(remainingPlayers[remainingPlayerCount].id == teamSample[teamSamplePlayerCount].id)

                remainingPlayers.pop(remainingPlayerCount)
        except:
            print("whoops " + str(remainingPlayerCount) + " " + str(teamSamplePlayerCount))

        teamSamplePlayerCount = teamSamplePlayerCount + 1
    remainingPlayerCount = remainingPlayerCount + 1
    
    print(len(remainingPlayers))

    # teams.append(teamSample)









# print(teams[3][1].name)


    # for members in teamSample:
    #     teamSample[member]

    # init.Team(teamSample,[])

    #add team to array

    

# for i in range(0,4):
#     print(str(i) + " " + team1[i].name)