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

# print(scanners)

print(len(scanners), "scanners read")

identity_matrix = [ [1,0,0,0],
                    [0,1,0,0],
                    [0,0,1,0],
                    [0,0,0,1]]

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


known_beacons = []
distances = []
transformations = []
known_scanners = []
for scanner_index in range(len(scanners)):
    beacon_distances = []
    scanner = scanners[scanner_index]
    for beacon1,beacon2 in itertools.combinations(scanner,2):
#        print(beacon1,beacon2)
        x1,y1,z1,one1 = beacon1
        x2,y2,z2,one2 = beacon2
        beacon_distances.append((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    beacon_distances.sort()
    distances.append(beacon_distances)


def get_common_distances(scanner_index_1, scanner_index_2):
    print(scanner_index_1,scanner_index_2)
    return set(distances[scanner_index_1]).intersection(distances[scanner_index_2])

def compare_scanner_distances(scanner_index_1, scanner_index_2):
    common = get_common_distances(scanner_index_1, scanner_index_2)
    return (len(common) >= 66)

def get_beacons_from_distances(common_distances: set, scanner_index):
    print("common distance count",len(common_distances))
    print(common_distances)
    dupe_distances = common_distances.copy()
    common_beacons = []
    foo = 0
    for beacon1,beacon2 in itertools.combinations(scanners[scanner_index],2):
        x1,y1,z1,one1 = beacon1
        x2,y2,z2,one2 = beacon2
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

def find_centroid(beacon_list: np.ndarray):
    centroid = np.zeros(4)
    for beacon in beacon_list:
         centroid = np.add(centroid,beacon)
    centroid = np.divide(centroid,len(beacon_list))
    return centroid



transformations.append(identity_matrix)
known_scanners.append(0)
for beacon in scanners[0]:
    known_beacons.append(beacon.tolist())

known_beacons.sort()
print(known_beacons)

test_scanner = 0
found_match = False
while test_scanner < len(scanners):
    print("testing scanner", test_scanner)
    if known_scanners.count(test_scanner) != 0:
        test_scanner += 1
        continue
    test_against_index = 0
    print("known scanners:",known_scanners)
    found_match = False
    while test_against_index < len(known_scanners) and not found_match:
        test_against = known_scanners[test_against_index]
        print("against", test_against)
        if not compare_scanner_distances(test_scanner, test_against):
            test_against_index += 1
            continue
        # ok, we match distances.  so now we need to try to match locations

        # First find the common points from the known scanner
        common_distances = get_common_distances(test_scanner,test_against)
        known_common_beacons = get_beacons_from_distances(common_distances,test_against)
        unknown_common_beacons = get_beacons_from_distances(common_distances,test_scanner)

        known_common_beacons.sort()
        print(known_common_beacons)


        known_centroid = find_centroid(known_common_beacons)
        unknown_centroid = find_centroid(unknown_common_beacons)

        print("known_centroid", known_centroid)
        print("unknown_centroid:", unknown_centroid)

        translate_matrix_1 = np.identity(4,dtype=float)
        translate_matrix_2 = np.identity(4,dtype=float)

        unknown_common_beacons_array = np.asarray(unknown_common_beacons)
        known_common_beacons_array = np.asarray(known_common_beacons)
        #print(unknown_common_beacons_array)
        #print(known_common_beacons_array)

        # first we need to translate by negative of the unknown centroid
        translate_unknown_centroid = np.negative(np.asarray(unknown_centroid))
        translate_unknown_centroid[3] = 1
        translate_known_centroid = np.asarray(known_centroid)
        translate_known_centroid[3] = 1
        translate_matrix_1[3] = translate_unknown_centroid
        translate_matrix_2[3] = translate_known_centroid

        rotation_index = 0
        while not found_match and rotation_index < 24:
            test_beacons = np.matmul(unknown_common_beacons_array,translate_matrix_1)
            test_beacons = np.matmul(test_beacons,rotations[rotation_index])
            test_beacons = np.matmul(test_beacons,translate_matrix_2)
            test_beacons_list = test_beacons.astype(int).tolist()
            test_beacons_list.sort()
            #print(test_beacons_list)
            #print(known_common_beacons)
            if test_beacons_list == known_common_beacons:
                found_match = True
            else:
                rotation_index += 1

        if not found_match:
            test_against_index += 1

        print(rotation_index)

    if not found_match:
        # If we got here then this unknown scanner doesn't have aknonwn match.  Check next scanner.
        test_scanner += 1
    else:
        # if we are here, we DID find a match
        # so now we need to transform all the beacons for the new scanner, put those in the beacon list, add the scanner to known scanners

        new_known_beacons = np.matmul(scanners[test_scanner],translate_matrix_1)
        new_known_beacons = np.matmul(new_known_beacons,rotations[rotation_index])
        new_known_beacons = np.matmul(new_known_beacons,translate_matrix_2)
        scanners[test_scanner] = np.add(new_known_beacons,0.5).astype(int)

        for beacon in new_known_beacons:
            known_beacons.append(np.add(beacon,0.5).astype(int).tolist())
        known_scanners.append(test_scanner)

        print("known beacons",known_beacons)

        # So now we need to start over again
        test_scanner = 0

print(scanners[4])
    
    







print("execution time (in ms): ",(time.process_time()-start_time)*1000) 
