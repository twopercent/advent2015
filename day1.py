#!/bin/env python3

floor = 0
position = 1

f = open('day1_data.txt', mode='r')
bracket = f.read(1)

while bracket != '':
    #print(bracket)
    if bracket == '(':
    #   print('up')
        floor += 1
    elif bracket == ')':
    #    print('down')
        floor -= 1

    if floor == -1:
        print('Basement at position ' + str(position))

    bracket = f.read(1)
    position += 1

print(floor)

f.close()
