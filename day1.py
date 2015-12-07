#!/bin/env python3

floor = 0

f = open('day1_data.txt', mode='r')
bracket = f.read(1)

while bracket != '':
    print(bracket)
    if bracket == '(':
        print('up')
        floor += 1
    if bracket == ')':
        print('down')
        floor -= 1
    bracket = f.read(1)

print(floor)

f.close()
