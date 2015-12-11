#!/bin/env python3

# Create a list of lists populated with False
# We assume all lights are off

grid = []

for x_light in range(4):
    grid_prep = []
    for y_light in range(4):
        grid_prep.append(False)
    grid.append(grid_prep)

# Open fhe data file
f = open('day6_testdata.txt', mode='r')

instruction = f.readline()[:-1]

def parse_instruction(order):
    order.split(' ')
    if 'on' in order:
        #Do something
    if 'off' in order:
        print('off')
    if 'toggle' in order:
        print('toggle')
    
    x1 = order[-3].split(',')[0]
    y1 = order[-3].split(',')[1]
    x2 = order[-1].split(',')[0]
    y2 = order[-1].split(',')[1]


# ON = True
# OFF = False
# TOGGLE = Current ^ True

def assert_light(x1, y1, x2, y2, operator):
    for x in range(x1,x2 + 1):
        for y in range(y1,y2 + 1):
            print('x ' + str(x) + ' y ' + str(y))
            if operator == 'on':
                grid[x][y] = True
            if operator == 'off':
                grid[x][y] = False
            if operator == 'toggle':
                grid[x][y] = grid[x][y] ^ True


print(instruction)

parse_instruction(instruction)

assert_light(0,0,1,3,'toggle')

print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])

f.close()

