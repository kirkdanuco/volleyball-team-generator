import os
import csv

#initialization variables
skillWeight = 0.75
heightWeight = 1 - skillWeight
teamSize = 4


cwd = os.path.dirname(os.path.abspath(__file__))
cwd = cwd + '\\files'
print(cwd)

# defining classes

class Player:
    def __init__(self, id, name, skill, height, playerRating, preferredPairing, forbiddenPairing):
        self.name = name
        self.id = id
        self.skill = skill
        self.height = height
        self.playerRating = skill * skillWeight + height * heightWeight

class Team:
    def __init__(self, players, averageRating):
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
                players.append(Player(row[0],row[1],int(row[2]),int(row[3]),[],[],[]))
                # print(players[count - 1].name)
                # print(players[count - 1].playerRating)

            count = count + 1

    return players