#!/bin/env python3

# Create a list of lists populated with False
# We assume all lights are off

grid = []
grid2 = []
on_count = 0
brightness_count = 0

# Create a grid of 'False' and a grid of '0'
print('Creating grids')
for x_light in range(1000):
    grid_prep = []
    grid_prep2 = []
    for y_light in range(1000):
        grid_prep.append(False)
        grid_prep2.append(0)
    grid.append(grid_prep)
    grid2.append(grid_prep2)

# Open fhe data file
print('Opening data file')
f = open('day6_data.txt', mode='r')

current_instruction = f.readline()[:-1]

def parse_instruction(instruction):
    instruction = instruction.split(' ')
    if 'on' in instruction:
        operator = 'on'
    if 'off' in instruction:
        operator = 'off'
    if 'toggle' in instruction:
        operator = 'toggle'
    
    #print(instruction)
    x1 = instruction[-3].split(',')[0]
    y1 = instruction[-3].split(',')[1]
    x2 = instruction[-1].split(',')[0]
    y2 = instruction[-1].split(',')[1]

# ON = True
# OFF = False
# TOGGLE = Current ^ True

    for x in range(int(x1),int(x2) + 1):
        for y in range(int(y1),int(y2) + 1):
            #print('x ' + str(x) + ' y ' + str(y))
            if operator == 'on':
                grid[x][y] = True
                grid2[x][y] += 1
            if operator == 'off':
                grid[x][y] = False
                if grid2[x][y] >= 1:
                    grid2[x][y] -= 1
            if operator == 'toggle':
                grid[x][y] = grid[x][y] ^ True
                grid2[x][y] += 2

print('Starting to parse')
while current_instruction != '':    
    parse_instruction(current_instruction)
    current_instruction = f.readline()[:-1]

f.close()

print('Calculating results')
for x_light in range(1000):
    for y_light in range(1000):
        if grid[x_light][y_light] == True:
            on_count += 1
        brightness_count += grid2[x_light][y_light]

print('Lights on ' + str(on_count))
print('Brightness ' + str(brightness_count))

#print('   0     1    2    3')
#print('0' + str(grid[0]))
#print('1' + str(grid[1]))
#print('2' + str(grid[2]))
#print('3' + str(grid[3]))

