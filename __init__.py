import os
import csv

#initialization variables
skillWeight = 0.75
heightWeight = 1 - skillWeight
teamSize = 7


cwd = os.path.dirname(os.path.abspath(__file__))
cwd = cwd + '\\files'
print(cwd)

# defining classes

class Player:
    def __init__(self, id, name, skill, height, playerRating, preferredPairing, forbiddenPairing, team):
        self.name = name
        self.id = int(id)
        self.skill = float(skill)
        self.height = float(height)
        self.playerRating = skill * skillWeight + height * heightWeight
        self.team = int(team)
    

class Team:
    def __init__(self, teamId, players, averageRating):
        self.teamId = int(teamId)
        self.players = players
        self.averageRating = averageRating


# defining functions

def extractPlayers():
    players = []
    with open(cwd + '\players.csv', newline='') as csvfile:
        delimitedReader = csv.reader(csvfile, delimiter=',') 
        count = 0 #skipping the header

        for row in delimitedReader:
            if count > 0:
                players.append(Player(row[0],row[1],int(row[2]),int(row[3]),[],[],[],0))
                # print(players[count - 1].name)
                # print(players[count - 1].playerRating)

            count = count + 1

    return players