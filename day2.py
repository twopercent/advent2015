#! /bin/env python3

f = open('day2_data.txt', mode='r')

paper_order = 0
ribbon_order = 0

dimensions = f.readline()[:-1]

while dimensions != '':
    dimension_list = dimensions.split('x')
    
    l = int(dimension_list[0])
    w = int(dimension_list[1])
    h = int(dimension_list[2])

    base_paper = 2*l*w + 2*w*h + 2*h*l
    # The area of the smallest side (the product of the smallest 2 dimensions)
    # is equal to the product of all dimensions divided by the largest side
    slack_paper = int(l*w*h / max(l,w,h))

    paper_order += base_paper + slack_paper    

    #It's bow time:
    int_list = [l,w,h]
    
    small = min(int_list)
    int_list.remove(small)

    medium = min(int_list)
    
    large = max(int_list)

    base_ribbon = small + small + medium + medium
    bow_ribbon = small * medium * large

    ribbon_order += base_ribbon + bow_ribbon

    dimensions = f.readline()[:-1]


f.close()
print('Total paper = ' + str(paper_order))
print('Total ribbon = ' + str(ribbon_order))
