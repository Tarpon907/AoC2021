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
#scanners = [np.array([list(map(int, p)) for p in re.findall("(-?\d+),(-?\d+),(-?\d+)", S)]) for S in scanners_str]

# print(scanners)

print(len(scanners), "scanners read")

identity_matrix = [ [1,0,0,0],
                    [0,1,0,0],
                    [0,0,1,0],
                    [0,0,0,1]]

temp_transform = np.zeros((24,3,3),dtype=int)
temp_transform[0]  =  [[ 1,  0,  0],\
                       [ 0,  1,  0],\
                       [ 0,  0,  1]]
temp_transform[1]  =  [[ 1,  0,  0],\
                       [ 0,  0, -1],\
                       [ 0, -1,  0]]
temp_transform[2]  =  [[ 1,  0,  0],\
                       [ 0, -1,  0],\
                       [ 0,  0, -1]]
temp_transform[3]  =  [[ 1,  0,  0],\
                       [ 0,  0, -1],\
                       [ 0,  1,  0]]
temp_transform[4]  =  [[-1,  0,  0],\
                       [ 0, -1,  0],\
                       [ 0,  0,  1]]
temp_transform[5]  =  [[-1,  0,  0],\
                       [ 0,  0,  1],\
                       [ 0,  1,  0]]
temp_transform[6]  =  [[-1,  0,  0],\
                       [ 0,  1,  0],\
                       [ 0,  0, -1]]
temp_transform[7]  =  [[-1,  0,  0],\
                       [ 0,  0, -1],\
                       [ 0, -1,  0]]
temp_transform[8]  =  [[ 0,  1,  0],\
                       [-1,  0,  0],\
                       [ 0,  0,  1]]
temp_transform[9]  =  [[ 0,  1,  0],\
                       [ 0,  0,  1],\
                       [ 1,  0,  0]]
temp_transform[10] =  [[ 0,  1,  0],\
                       [ 1,  0,  0],\
                       [ 0,  0, -1]]
temp_transform[11] =  [[ 0,  1,  0],\
                       [ 0,  0, -1],\
                       [-1,  0,  0]]
temp_transform[12] =  [[ 0, -1,  0],\
                       [ 1,  0,  0],\
                       [ 0,  0,  1]]
temp_transform[13] =  [[ 0, -1,  0],\
                       [ 0,  0,  1],\
                       [-1,  0,  0]]
temp_transform[14] =  [[ 0, -1,  0],\
                       [-1,  0,  0],\
                       [ 0,  0, -1]]
temp_transform[15] =  [[ 0, -1,  0],\
                       [ 0,  0, -1],\
                       [ 1,  0,  0]]
temp_transform[16] =  [[ 0,  0, -1],\
                       [ 0,  1,  0],\
                       [ 1,  0,  0]]
temp_transform[17] =  [[ 0,  0, -1],\
                       [-1,  0,  0],\
                       [ 0,  1,  0]]
temp_transform[18] =  [[ 0,  0, -1],\
                       [ 0, -1,  0],\
                       [-1,  0,  0]]
temp_transform[19] =  [[ 0,  0, -1],\
                       [ 1,  0,  0],\
                       [ 0, -1,  0]]
temp_transform[20] =  [[ 0,  0,  1],\
                       [ 0,  1,  0],\
                       [-1,  0,  0]]
temp_transform[21] =  [[ 0,  0,  1],\
                       [-1,  0,  0],\
                       [ 0, -1,  0]]
temp_transform[22] =  [[ 0,  0,  1],\
                       [ 0, -1,  0],\
                       [ 1,  0,  0]]
temp_transform[23] =  [[ 0,  0,  1],\
                       [ 1,  0,  0],\
                       [ 0,  1,  0]]

rotations = np.ndarray((24,4,4),dtype = int)
for i in range(24):
    rotations[i] = np.identity(4,dtype=int)
    foo = temp_transform[i]
    bar = rotations[i]
    bar[0:foo.shape[0], 0:foo.shape[1]] = foo


distances = []
transformations = []
known_scanners = []
matching_rotations = set()
for scanner_index in range(len(scanners)):
    beacon_distances = []
    scanner = scanners[scanner_index]
    for beacon1,beacon2 in itertools.combinations(scanner,2):
#        print(beacon1,beacon2)
        x1,y1,z1,one = beacon1
        x2,y2,z2,one = beacon2
        beacon_distances.append((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    beacon_distances.sort()
    if len(beacon_distances) != len(set(beacon_distances)):
        print("SNEAKY BASTARD FOUND:",scanner_index)
    distances.append(beacon_distances)
            
            


def get_common_distances(scanner_index_1, scanner_index_2):
    print(scanner_index_1,scanner_index_2)
    return set(distances[scanner_index_1]).intersection(distances[scanner_index_2])

def compare_scanner_distances(scanner_index_1, scanner_index_2):
    common = get_common_distances(scanner_index_1, scanner_index_2)
    return (len(common) >= 66)


def find_three_beacons(distance_list: set, scanner_index):
    dupe_distances = distance_list.copy()
    common_beacons = []
    points_found = 0
    for beacon1, beacon2 in itertools.combinations(scanners[scanner_index],2):
        x1,y1,z1,one = beacon1
        x2,y2,z2,one = beacon2
        distance = (x2-x1)**2+(y2-y1)**2+(z2-z1)**2
        if distance in dupe_distances:
            dupe_distances.remove(distance)
            b1 = beacon1.tolist()
            b2 = beacon2.tolist()
            common_beacons.append(b1)
            common_beacons.append(b2)
            break
    print(common_beacons)
    for beacon1, beacon2 in itertools.combinations(scanners[scanner_index],2):
        b1 = beacon1.tolist()
        b2 = beacon2.tolist()
        if common_beacons.count(b1) == 0 and common_beacons.count(b2) == 0:
            continue
        if common_beacons.count(b1) != 0 and common_beacons.count(b2) != 0:
            continue
        x1,y1,z1,one = beacon1
        x2,y2,z2,one = beacon2
        distance = (x2-x1)**2+(y2-y1)**2+(z2-z1)**2
        if distance in dupe_distances:
            dupe_distances.remove(distance)
            if common_beacons.count(b1):
                common_beacons.append(b2)
            elif common_beacons.count(b2):
                common_beacons.append(b1)
            break

    common_beacons.sort()
#    print(common_beacons)
    return(common_beacons)

def find_three_coresponding_beacons(scanner_id_1,scanner_id_2):
    common_distances = get_common_distances(scanner_id_1,scanner_id_2)
    three_beacons_1 = find_three_beacons(common_distances,scanner_id_1)
    x1,y1,z1,one = three_beacons_1[0]
    x2,y2,z2,one = three_beacons_1[1]
    x3,y3,z3,one = three_beacons_1[2]
    new_distances = set()
    d1 = (x2-x1)**2+(y2-y1)**2+(z2-z1)**2

    new_distances.add(d1)
    new_distances.add((x3-x1)**2+(y3-y1)**2+(z3-z1)**2)
    new_distances.add((x3-x2)**2+(y3-y2)**2+(z3-z2)**2)
    print(three_beacons_1,new_distances)
    three_beacons_2 = find_three_beacons(new_distances,scanner_id_2)
    x3,y3,z3,one = three_beacons_2[0]
    x4,y4,z4,one = three_beacons_2[1]
    d2 = (x3-x4)**2+(y3-y4)**2+(z3-z4)**2
    print(d1,d2)

    if d1 != d2:
        three_beacons_2.sort(reverse=True)
 

    print(three_beacons_2,new_distances)

    return([three_beacons_1,three_beacons_2])





def get_beacons_from_distances(common_distances: set, scanner_index):
    print("common distance count",len(common_distances))
    print(common_distances)
    dupe_distances = common_distances.copy()
    common_beacons = []
    foo = 0
    for beacon1,beacon2 in itertools.combinations(scanners[scanner_index],2):
        x1,y1,z1 = beacon1
        x2,y2,z2 = beacon2
        distance = (x2-x1)**2+(y2-y1)**2+(z2-z1)**2
        if distance in common_distances:
            dupe_distances.remove(distance)
            foo += 1
            b1 = beacon1.tolist()
            b2 = beacon2.tolist()
            if common_beacons.count(b1) == 0:
                common_beacons.append(b1)
            if common_beacons.count(b2) == 0:
                common_beacons.append(b2)

    print(scanner_index,foo,common_beacons,dupe_distances)
    return common_beacons


known_beacons = []
known_scanners = [0]
known_beacons = scanners[0].tolist()
print(known_beacons)
unknown_scanners = []
known_scanner_coords = [[0,0,0]]
tested_pairs = []

# print(known_scanners)
# print(known_beacons)

for foo in range(1,len(scanners)):
    unknown_scanners.append(foo)

print ("unknown_scanners",unknown_scanners)

transformations = []
test_index = 0
test_against_index = 0
while len(unknown_scanners) > 0:
    test_id = unknown_scanners[test_index]
    print("test_id",test_id)
    test_against_index = 0
    found_match = False
    while test_against_index < len(known_scanners) and not found_match:
        test_against_id = known_scanners[test_against_index]
        print("test_against_id",test_against_id)
        if test_id == test_against_id:
            test_against_index += 1
            continue
        if tested_pairs.count([test_id,test_against_id]):
            test_against_index += 1
            continue
        tested_pairs.append([test_id,test_against_id])
        if not compare_scanner_distances(test_id,test_against_id):
            test_against_index += 1
            continue
        common_distances = get_common_distances(test_id, test_against_id)
        test_triad,test_against_triad = find_three_coresponding_beacons(test_id,test_against_id)

        test_triad_array = np.asarray(test_triad)
        test_against_triad_array = np.asarray(test_against_triad)

        t4 = np.identity(4,dtype = int)
        t4_against = np.identity(4, dtype = int)
        
        foo = test_triad_array
        t4[0:foo.shape[0], 0:foo.shape[1]] = foo

        foo = test_against_triad_array
        t4_against[0:foo.shape[0], 0:foo.shape[1]] = foo
        print("testing against:",t4_against)

        rotation_index = 0
        found_transformation = False
        while rotation_index < 24 and not found_transformation:
            new_t4 = np.matmul(t4,rotations[rotation_index])
#            print(new_t4)

            difference = np.subtract(t4_against[1],new_t4[1])
            difference[3] = 1
            translate_matrix = np.identity(4,dtype=int)
            translate_matrix[3] = difference
#            print(translate_matrix)
            new_t4_x = np.matmul(new_t4,translate_matrix)
            print(t4_against[0])
            print(new_t4_x[0],"\n")

            if new_t4_x[0].tolist() == t4_against[0].tolist()  and new_t4_x[2].tolist() == t4_against[2].tolist():
                found_transformation = True
                transformation = np.matmul(rotations[rotation_index],translate_matrix)
                print(transformation)
                print(new_t4_x)
                transformations.append(transformation)
            else:
                rotation_index += 1
        if not found_transformation:
            print("Shit went bad")
            exit()
        
        new_known_beacons = np.matmul(scanners[test_id],transformation)
        scanners[test_id] = new_known_beacons

        print(known_beacons)
        new_known_beacons.tolist()
        for beacon in new_known_beacons:
            b = beacon.tolist()
            if known_beacons.count(b) == 0:
                known_beacons.append(b)

        print(known_beacons)
        known_scanners.append(test_id)
        unknown_scanners.remove(test_id)




        test_against_index += 1
    test_index  = (test_index + 1) % len(unknown_scanners)



print("execution time (in ms): ",(time.process_time()-start_time)*1000) 
