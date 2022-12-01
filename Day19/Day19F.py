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

identity = np.identity(4,dtype=int)
known_beacons = []
known_scanners = []
unknown_scanners = []

temp_transform = np.zeros((24,3,3),dtype=int)
temp_transform[0]  =  [[ 1,  0,  0],\
                       [ 0,  1,  0],\
                       [ 0,  0,  1]]
temp_transform[1]  =  [[ 1,  0,  0],\
                       [ 0,  0,  1],\
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



def read_input():
    with open("c:/users/ted/VSCode/AoC2021/Day19/input.txt", 'r') as file:
        input = file.read()

    scanners_str = input.split("\n\n")
    scanners = [np.array([list(map(int, p)) + [1] for p in re.findall("(-?\d+),(-?\d+),(-?\d+)", S)]) for S in scanners_str]
    #scanners = [np.array([list(map(int, p)) for p in re.findall("(-?\d+),(-?\d+),(-?\d+)", S)]) for S in scanners_str]

    # #print(scanners)

    return scanners

def calculate_beacon_distances(scanners):
    distances = []
    for scanner_index in range(len(scanners)):
        beacon_distances = []
        scanner = scanners[scanner_index]
        for beacon1,beacon2 in itertools.combinations(scanner,2):
    #        #print(beacon1,beacon2)
            x1,y1,z1,one1 = beacon1
            x2,y2,z2,one2 = beacon2
            beacon_distances.append((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
        beacon_distances.sort()
        distances.append(beacon_distances)
    return distances

def add_scanner_to_beacons_with_transformation(scanner, beacon_list, transformation):
    new_beacons = np.matmul(scanner,transformation)
    for beacon in new_beacons:
        b = beacon.tolist()
        if beacon_list.count(b) == 0:
            beacon_list.append(b)
    return(new_beacons)


def get_distance(beacon1, beacon2):
    x1,y1,z1,one = beacon1
    x2,y2,z2,one = beacon2
    distance = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
    return distance
 


def get_common_distances(scanner_index_1, scanner_index_2):
    #print(scanner_index_1,scanner_index_2)
    return set(distances[scanner_index_1]).intersection(distances[scanner_index_2])


def get_beacons(scanner_index, cd_set:set):
    test_scanner = scanners[scanner_index]
    beacons = []
    for beacon1,beacon2 in itertools.combinations(test_scanner,2):
        test_distance = get_distance(beacon1,beacon2)
        if test_distance in cd_set:
            b1 = beacon1.tolist()
            b2 = beacon2.tolist()
            if beacons.count(b1) == 0:
                beacons.append(b1)
            if beacons.count(b2) == 0:
                beacons.append(b2)
    return(beacons)

def get_beacon_distance_list(reference_beacon, beacon_list):
    bdl = []
    for beacon in beacon_list:
        distance = get_distance(reference_beacon,beacon)
        bdl.append([distance,beacon])

    bdl.sort()

    return bdl
 



def get_common_beacons(scanner_index_1, scanner_index_2, cd_set:set):
    test_scanner = scanners[scanner_index_1]
    test_against_scanner = scanners[scanner_index_2]

    test_beacons = get_beacons(scanner_index_1,cd_set)
    test_against_beacons = get_beacons(scanner_index_2,cd_set)

    test_beacons.sort()

    #print(test_beacons)
    #print(test_against_beacons)


    test_bdl = get_beacon_distance_list(test_beacons[0], test_beacons)
    d1 = test_bdl[1][0]
    d2 = test_bdl[2][0]
    for reference in test_against_beacons:
        ta_bdl = get_beacon_distance_list(reference,test_against_beacons)
        ta_d1 = ta_bdl[1][0]
        ta_d2 = ta_bdl[2][0]

        if ta_d1 == d1 and ta_d2 == d2:
            break

    #print(test_bdl)
    #print(ta_bdl)

    test_beacons = np.asarray([item[1] for item in test_bdl])
    test_against_beacons = np.asarray([item[1] for item in ta_bdl])

    #print("\n",test_beacons)
    #print(test_against_beacons)

    return(test_beacons,test_against_beacons)


def add_scanner_to_scanner_list(scanner_list,transformation):
    zero = np.asarray([0,0,0,1])
    coords = np.matmul(zero,transformation)
    scanner_list.append(coords.tolist())



scanners = read_input()


distances = calculate_beacon_distances(scanners)

scanner_coords = [[0,0,0,1]]

add_scanner_to_beacons_with_transformation(scanners[0],known_beacons,identity)
known_scanners = [0]
for i in range(1,len(scanners)):
    unknown_scanners.append(i)
#print(known_beacons)
#print(known_scanners)
#print(unknown_scanners)


us_index = 0
tested = []
while len(unknown_scanners) > 0:
    found_match = False
    test_index = unknown_scanners[us_index]
    ks_index = 0
    while not found_match and ks_index < len(known_scanners):
        test_against_index = known_scanners[ks_index]
        if tested.count([test_index, test_against_index]) != 0:
            ks_index += 1
            continue
        cd = get_common_distances(test_index,test_against_index)
        #print(len(cd))
        if len(cd) >= 66:
            if len(cd) > 66:
                print(len(cd))
            test_beacons,test_against_beacons = get_common_beacons(test_index, test_against_index, cd)
            tb1 = test_beacons[0:4]
            #print(tb1)
            tb2 = test_against_beacons[0:4]
            #print(tb2)

            diff1 = np.negative(tb1[0])
            diff1[3] = 1
            trans_mat_1 = np.identity(4,dtype=int)
            trans_mat_1[3] = diff1
            diff2 = np.negative(tb2[0])
            diff2[3] = 1
            trans_mat_2 = np.identity(4,dtype = int)
            trans_mat_2[3] = diff2
            diff3 = tb2[0]
            diff3[3] = 1
            trans_mat_3 = np.identity(4,dtype = int)
            trans_mat_3[3] = diff3
            

            temp_tb1 = np.matmul(tb1,trans_mat_1)
            temp_tb2 = np.matmul(tb2,trans_mat_2)
            #print(temp_tb1,"\n",temp_tb2)

            rotation_index = 0
            found_rotation = False
            while rotation_index < 24 and not found_rotation:
                tb1_rot = np.matmul(temp_tb1,rotations[rotation_index])
                if np.array_equal(tb1_rot,temp_tb2):
                    found_rotation = True
                else:
                    rotation_index += 1

            if found_rotation:
                transformation = np.matmul(trans_mat_1,rotations[rotation_index])
                transformation = np.matmul(transformation,trans_mat_3)
                #print(transformation)
                new_tb1 = np.matmul(tb1,transformation)
                scanners[test_index] = add_scanner_to_beacons_with_transformation(scanners[test_index],known_beacons,transformation)
                add_scanner_to_scanner_list(scanner_coords,transformation)
                #print("test_index is",test_index)
                #print("unknown_scanners is", unknown_scanners)
                known_scanners.append(test_index)
                unknown_scanners.remove(test_index)
                #print("unknown_scanners is now", unknown_scanners)
                #print("known_scanners is now  ", known_scanners)
                found_match = True
            else:
                #print("SHIT WENT BAD")
                exit()
                
        ks_index += 1
    if len(unknown_scanners):
        us_index = (us_index + 1) % len(unknown_scanners)

    known_beacons.sort()
    #print(np.asarray(known_beacons))
print(len(known_beacons))
print(scanner_coords)
max_distance = 0

for scanner1,scanner2 in itertools.combinations(scanner_coords,2):
    x1,y1,z1,one = scanner1
    x2,y2,z2,one = scanner2
    distance = abs(x2-x1)+abs(y2-y1)+abs(z2-z1)
    max_distance = max(max_distance,distance)

print(max_distance)

new_distance_list =[]
for beacon1, beacon2 in itertools.combinations(known_beacons,2):
    x1,y1,z1,one = beacon1
    x2,y2,z2,one = beacon2
    distance = (x2-x1)**2+(y2-y1)**2+(z2-z1)**2
    new_distance_list.append(distance)
    
new_distance_set = set(new_distance_list)
print (len(new_distance_set))


    
    



print("execution time (in ms): ",(time.process_time()-start_time)*1000) 
