#!/bin/env python3

known_wires = {}
operators = ['AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT']
    
# Were going to remove instructins from the list as they are processes
# so we create an array that we can modify
def getInstructions(filename):
    instruction_array = []
    f = open(filename, mode='r')

    # Use split to dump the newline
    line = f.readline()[:-1]
    while line != '':
        instruction_array.append(line)
        line = f.readline()[:-1]
    f.close()
    return instruction_array

def getAvailableInstructions(ri, kw, op):
    # Here we will figure out what instructions we can complete
    # Split instructions to get inputs only
    for line in ri:
        known_inputs = True
        operator = ''
        operands = []
        inputs = line.split(' -> ')[0].split(' ')
        output = line.split(' -> ')[1]
    # For each item in the inputs, it is is a wire and not in known wires, we cannot compute the instructino
        for items in inputs:
            if items in op:
                operator = items 
            elif items.isdecimal() or items in kw:
                if items.isdecimal():
                    operands.append(items)
                else:
                    operands.append(kw[items])
            else:
                known_inputs = False

        if known_inputs == True:
            print('Good insctuction: ' + str(line))

            # Assign the value to known wires
            if operator == '':
                kw[output] = inputs[0]

            elif operator == 'AND':
                kw[output] = int(inputs[0]) & int(inputs[1])
            
            elif operator == 'OR':
                kw[output] = int(inputs[0]) | int(inputs[1])
            
            elif operator == 'NOT':
                kw[output] = ~ inputs[0]
            
            elif operator == 'LSHIFT':
                kw[output] = inputs[0] << inputs[1]
            
            elif operator == 'RSHIFT':
                kw[output] = inputs[0] >> inputs[1]

            # Remove the instruction fom ri
            ri.remove(line)

    print(kw)
    return inputs

def completeAvailable(ri, kw):
    null





instructions = getInstructions('day7_data.txt')
inputs = getAvailableInstructions(instructions, known_wires, operators)

