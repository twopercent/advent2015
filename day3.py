#!/bin/env python3

f = open('day3_data.txt', mode='r')

solo_santa = [0,0]
house_list = [[0,0]]

team_santa = [0,0]
robo_santa = [0,0]
team_houses = [[0,0]]

index = 0

current_direction = f.read(1)

def move(direction, who, houses):
    #west
    if direction == '<':
        who[0] = who[0] - 1
    #east
    if direction == '>':
        who[0] = who[0] + 1
    #north
    if direction == '^':
        who[1] = who[1] + 1
    #south
    elif direction == 'v':
        who[1] = who[1] - 1

    if who not in houses:
        houses.append([who[0],who[1]])


while current_direction != '':
    move(current_direction, solo_santa, house_list)
    if index % 2 == 0:
        move(current_direction, team_santa, team_houses)
    else:
        move(current_direction, robo_santa, team_houses)

    index += 1
    current_direction = f.read(1)


    

print("Santa's final position " + str(solo_santa))
print("Team Santa's final position" + str(team_santa))
print("Robo Santa's final position " + str(solo_santa))

print("Length of Santa's house list " + str(len(house_list)))
print("Length of Team Santa and Robo Santa's house list " + str(len(team_houses)))

f.close()
