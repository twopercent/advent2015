#!/bin/env python3

import hashlib

index = 0
print('Computing...\n')

while True:

    byte_index = str(index).encode('utf-8')
    m = hashlib.md5(b"yzbqklnj" + byte_index)
    #print(m.hexdigest())
    
    if m.hexdigest()[0:5] == '00000':
        print('5 zero index = ' + str(index))
        break
    
    index += 1


while True:

    byte_index = str(index).encode('utf-8')
    m = hashlib.md5(b"yzbqklnj" + byte_index)
    #print(m.hexdigest())
    
    if m.hexdigest()[0:6] == '000000':
        print('6 zero index = ' + str(index))
        break
    
    index += 1
