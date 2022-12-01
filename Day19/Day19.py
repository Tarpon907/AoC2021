import scipy as sp
from mpl_toolkits import mplot3d
import matplotlib.pylab as plt
import numpy as np
import re
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


start_time = time.process_time()

lines = open('c:/users/ted/VSCode/AoC2021/Day19/input.txt', 'r').readlines()
colors=["#ff0000","#00ff00","0000ff","#ffff00","#ff00ff","#00ffff"]

temp_transform = np.zeros((24,3,3),dtype=int)
temp_transform[0]  = [[ 1,  0,  0],\
                       [ 0,  1,  0],\
                       [ 0,  0,  1]]
temp_transform[1]  = [[ 1,  0,  0],\
                       [ 0,  0, -1],\
                       [ 0, -1,  0]]
temp_transform[2]  = [[ 1,  0,  0],\
                       [ 0, -1,  0],\
                       [ 0,  0, -1]]
temp_transform[3]  = [[ 1,  0,  0],\
                       [ 0,  0, -1],\
                       [ 0,  1,  0]]
temp_transform[4]  = [[-1,  0,  0],\
                       [ 0, -1,  0],\
                       [ 0,  0,  1]]
temp_transform[5]  = [[-1,  0,  0],\
                       [ 0,  0,  1],\
                       [ 0,  1,  0]]
temp_transform[6]  = [[-1,  0,  0],\
                       [ 0,  1,  0],\
                       [ 0,  0, -1]]
temp_transform[7]  = [[-1,  0,  0],\
                       [ 0,  0, -1],\
                       [ 0, -1,  0]]
temp_transform[8]  = [[ 0,  1,  0],\
                       [-1,  0,  0],\
                       [ 0,  0,  1]]
temp_transform[9]  = [[ 0,  1,  0],\
                       [ 0,  0,  1],\
                       [ 1,  0,  0]]
temp_transform[10] = [[ 0,  1,  0],\
                       [ 1,  0,  0],\
                       [ 0,  0, -1]]
temp_transform[11] = [[ 0,  1,  0],\
                       [ 0,  0, -1],\
                       [-1,  0,  0]]
temp_transform[12] = [[ 0, -1,  0],\
                       [ 1,  0,  0],\
                       [ 0,  0,  1]]
temp_transform[13] = [[ 0, -1,  0],\
                       [ 0,  0,  1],\
                       [-1,  0,  0]]
temp_transform[14] = [[ 0, -1,  0],\
                       [-1,  0,  0],\
                       [ 0,  0, -1]]
temp_transform[15] = [[ 0, -1,  0],\
                       [ 0,  0, -1],\
                       [ 1,  0,  0]]
temp_transform[16] = [[ 0,  0, -1],\
                       [ 0,  1,  0],\
                       [ 1,  0,  0]]
temp_transform[17] = [[ 0,  0, -1],\
                       [-1,  0,  0],\
                       [ 0,  1,  0]]
temp_transform[18] = [[ 0,  0, -1],\
                       [ 0, -1,  0],\
                       [-1,  0,  0]]
temp_transform[19] = [[ 0,  0, -1],\
                       [ 1,  0,  0],\
                       [ 0, -1,  0]]
temp_transform[20] = [[ 0,  0,  1],\
                       [ 0,  1,  0],\
                       [-1,  0,  0]]
temp_transform[21] = [[ 0,  0,  1],\
                       [-1,  0,  0],\
                       [ 0, -1,  0]]
temp_transform[22] = [[ 0,  0,  1],\
                       [ 0, -1,  0],\
                       [ 1,  0,  0]]
temp_transform[23] = [[ 0,  0,  1],\
                       [ 1,  0,  0],\
                       [ 0,  1,  0]]

rotations = np.ndarray((24,4,4),dtype = int)
for i in range(24):
    rotations[i] = np.identity(4,dtype=int)
    foo = temp_transform[i]
    bar = rotations[i]
    bar[0:foo.shape[0], 0:foo.shape[1]] = foo
    logging.info(rotations[i])

i = 0
scanner_count = 0
point_list_for_scanner = []
known_points = []
scanner_list = []
scanner_coordinates = []
found_scanners = []
while i < len(lines):
    line = lines[i].strip()
    if not len(line):
        i += 1
        continue
    if line.find("scanner") != -1:
        if scanner_count:
            scanner_array = np.array([[e[0],e[1],e[2],1] for e in point_list_for_scanner])
            point_list_for_scanner = []
            scanner_list.append(scanner_array)
        scanner_count += 1
    else:
        point = [int(x) for x in line.split(",")]
        point_list_for_scanner.append(point)
#        print(point_list_for_scanner)
    i += 1

scanner_array = np.array([[e[0],e[1],e[2],1] for e in point_list_for_scanner])
scanner_list.append(scanner_array)
scanner_count += 1


# compare 2 scanners at a time.
# 

for point in scanner_list[0]:
    known_points.append(point.tolist())

found_scanners.append(scanner_list[0])
scanner_list.remove(scanner_list[0])
print("found scanners:",found_scanners)
print("unknown scanners:",scanner_list)


found_list_index = 0


for known_scanner in found_scanners:
    new_found_scanner_list = []
#    print(scanner_list[i])
    for unknown_scanner_index in range(len(scanner_list)):
        unknown_scanner = scanner_list[unknown_scanner_index]
        # logging.debug("comparing scanner",i,"and scanner",j)
        # so we are comparing scanner i and scanner j.
        # leave scanner i in its current orientation and transform scanner j to see if we match
        found_match = False
        transformcount = 0
        rotationcount = 0
        for rotation in rotations:
#            print(rotation)
            rotationcount += 1
            rotated_scanner_2 = np.matmul(unknown_scanner,rotation)
            # now we need to translate it so a point lines up
            # loop over points for each scanner and line up scanner 2 with scanner 1
            for known_point in known_scanner:
                for test_point in rotated_scanner_2:
                    difference = np.subtract(known_point,test_point,dtype=int)
                    difference[3] = 1
                    translation_matrix = np.identity(4,dtype=int)
                    translation_matrix[3] = difference


                    translated_2 = np.matmul(rotated_scanner_2,translation_matrix)
                    # now iterate over the points on the 2 scanners and see if 12 points match

#                    print("comparing:\n",known_scanner,"and\n",translated_2)
                    num_match = 0
                    num_left = len(translated_2)
                    for iter1 in translated_2:

                        for iter2 in known_scanner:
#                            print(iter1,iter2)
                            if np.array_equal(iter1,iter2):
#                                print(iter1,"in scanner",i,"list")
                                num_match += 1
#                                print(num_match)
                        num_left -= 1
                        if num_left + num_match < 12:
                            break    
#                    print(i,j,k,l,transformcount,num_match)
                    if num_match >= 12:
                        print("found a match")
                        found_match = True
                        last_translation = np.matmul(rotation,translation_matrix)
#                        print("transforming match\n",unknown_scanner,"\n",translated_2)
                        found_scanners.append(translated_2)
                        new_found_scanner_list.insert(0, unknown_scanner_index)
                        for point in translated_2:
                            known_points.append(point.tolist())
                        print("known scanners:",len(found_scanners)," new found scanners list:", new_found_scanner_list, "unknown scanner list length:", len(scanner_list))
                        break
                if found_match:
                    break
            if found_match:
                break
    if new_found_scanner_list is not None:
        for i in new_found_scanner_list:
            scanner_list.pop(i)

print(len(known_points), known_points)

known_points.sort()

for point in known_points:
    print(point)

i = 0
for point in known_points:
    while i < len(known_points) - 1 and known_points[i+1] == known_points[i]:
        known_points.pop(i+1)
    i += 1
#    while known_points.count(point) > 1:
#        known_points.remove(point)
#

for point in known_points:
    print(point)
print(len(known_points))



        
    



print("execution time (in ms): ",(time.process_time()-start_time)*1000) 
