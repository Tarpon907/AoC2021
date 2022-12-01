import scipy as sp
from mpl_toolkits import mplot3d
import matplotlib.pylab as plt
import numpy as np
import re
import time
import logging
import itertools

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


start_time = time.process_time()

with open("c:/users/ted/VSCode/AoC2021/Day19/sample.txt", 'r') as file:
    input = file.read()

scanners_str = input.split("\n\n")
scanners = [np.array([list(map(int, p)) + [1] for p in re.findall("(-?\d+),(-?\d+),(-?\d+)", S)]) for S in scanners_str]

print(scanners)

beacons = []
for p in scanners[0]:
    beacons.append(p.tolist())

mapped_scanners = [0]

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

print(rotations)

def d_sq(point1, point2, size=4):
    if size == 4:
        x1,y1,z1,one = point1
        x2,y2,z2,one = point2

    else:
        x1,y1,z1 = point1
        x2,y2,z2 = point2
    return (x1-x1)**2+(y2-y1)**2+(z2-z1)**2

def align_scanners(mapped, unmapped):

#    print(mapped)
#    print(unmapped)

    global beacons
    global rotations
    found_match = False
    transformcount = 0
    rotationcount = 0
    unmapped_pairs = []
    mapped_pairs = []
    match_count = 0
    mapped_points = []
    unmapped_points = []

    for (i,j) in itertools.combination(unmapped,2):
        d_unmapped = d_sq(unmapped[i],unmapped[j])
        for (k,l) in itertools.combination(mapped,2):
            d_mapped = d_sq(mapped[k],mapped[l])
            if d_unmapped == d_mapped:
                unmapped_pairs.append([unmapped[i],unmapped[j]])
                mapped_pairs.append([mapped[k],mapped[l]])
                if mapped_points.count(mapped[k]) == 0:
                    mapped_points.append(mapped[k])
                if mapped_points.count(mapped[l]) == 0:
                    mapped_points.append(mapped[l])
                if unmapped_points.count(unmapped[i]) == 0:
                    mapped_points.append(mapped[i])
                if unmapped_points.count(unmapped[j]) == 0:
                    unmapped_points.append(unmapped[j])
    unmapped_points_array = np.array([list(map(int, p)) + [1] for p in unmapped_points])
    mapped_points_array = np.array([list(map(int, p)) + [1] for p in mapped_points])
    
   

    mapped_centroid = []
    unmapped_centroid = []
    for unmapped_point in unmapped_points:
        x,y,z,one = unmapped_point
        unmapped_centroid[0] += x
        unmapped_centroid[1] += y
        unmapped_centroid[2] += z
        unmapped_centroid[3] = 1
    for mapped_point in mapped_points:
        x,y,z,one = mapped_point
        mapped_centroid[0] += x
        mapped_centroid[1] += y
        mapped_centroid[2] += z
        mapped_centroid[3] = 1
    difference = np.subtract(mapped_centroid,unmapped_centroid,dtype=int)
    difference[3] = 1
    translation_matrix = np.identity(4,dtype=int)
    translation_matrix[3] = difference
    translated_2 = np.matmul(rotated_scanner_2,translation_matrix)
               

            



    for rotation in rotations:
#        print(rotation)
        rotationcount += 1
        rotated_scanner_2 = np.matmul(unmapped,rotation)
        # now we need to translate it so a point lines up
        # loop over points for each scanner and line up scanner 2 with scanner 1
        for known_point in mapped:
#            print(known_point)
            for test_point in rotated_scanner_2:
                difference = np.subtract(known_point,test_point,dtype=int)
                difference[3] = 1
                translation_matrix = np.identity(4,dtype=int)
                translation_matrix[3] = difference
                translated_2 = np.matmul(rotated_scanner_2,translation_matrix)
                # now iterate over the points on the 2 scanners and see if 12 points match

#                    print("comparing:\n",known_scanner,"and\n",translated_2)
                num_match = 0
                for iter1 in translated_2:
                    for iter2 in mapped:
#                        print(iter1,iter2)
                        if np.array_equal(iter1,iter2):
#                                print(iter1,"in scanner",i,"list")
                            num_match += 1   
#                    print(i,j,k,l,transformcount,num_match)
#                print("num_match:",num_match)
                if num_match >= 12:
                    print("found a match")
                    found_match = True
                    last_translation = np.matmul(rotation,translation_matrix)
#                        print("transforming match\n",unknown_scanner,"\n",translated_2)
                    for point in translated_2:
                        duplicate = False
                        for x in beacons:
                            if np.array_equal(x,point):
                                duplicate = True
                        if not duplicate:
                            beacons.append(point.tolist())
                    break
                if found_match:
                    break
            if found_match:
                break
        if found_match:
            break    
    return translated_2

distances = []
i = 0
for scanner in scanners:
    distance = []
    for (i,j) in itertools.combinations(range(len(scanner)),2):
#        print(i,j)
        if i == j:
            continue
        distance.append(d_sq(scanner[i],scanner[j]))
        #print(distance)
    distances.append(distance)
    #print(distances)


matches = []
for i,j in itertools.combinations(range(len(distances)),2):
    count = 0
    for k,l in itertools.product(range(len(distances[i])),range(len(distances[j]))):
        if distances[i][k] == distances[j][l]:
            count += 1
    if count >= 22:
        print(i, "and", j, "match")
        matches.append([i,j])

print(matches)


while len(matches) > 0:
    print("mapped:",mapped_scanners)
    print("remaining:",len(matches))
    for i in mapped_scanners:
        for j in (matches):
            if j.count(i):

                if j[0] == i:
                    print("aligning",j[1], "to", j[0])
                    scanners[j[1]] = align_scanners(scanners[j[0]],scanners[j[1]])
                    mapped_scanners.append(j[1])
                else:
                    print("aligning",j[0], "to", j[1])
                    scanners[j[0]] = align_scanners(scanners[j[1]],scanners[j[0]])
                    mapped_scanners.append(j[0])
                matches.remove(j)
                print(len(matches), "remaining")

beacons.sort()
for x in beacons:
    while beacons.count(x) > 1:
        beacons.remove(x)

for x in beacons:
    print(x)
#print(beacons)

print(len(beacons))



                


print("execution time (in ms): ",(time.process_time()-start_time)*1000) 
