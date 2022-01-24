import scipy as sp
import matplotlib.pylab as plt
import numpy as np

lines = open('c:/users/ted/AoC/AoC2021/Day12/input.txt', 'r').readlines()

pathlist = []

def find_paths(current_path,node,used_our_one):
    print (current_path, " -> ", node)
    if node == 'start' and len(current_path) > 0:
        return 0
    if node == 'end':
        current_path.append(node)
        print("path found: ", current_path)
        current_path.pop()
        return 1
    if node.islower() and current_path.count(node) > 0:
        if used_our_one:
            return 0
        else:
            used_our_one = True

    index = 0
    found = False
    while not found:
        name, neighbors = pathlist[index]
        if name == node:
            found = True
        index += 1

    current_path.append(node)
    retval = 0
 
    for neighbor in neighbors:
        print("neighbors of ",node,": ",neighbors, " | ", neighbor)
        retval += find_paths(current_path,neighbor,used_our_one)
    current_path.pop()
    return retval



for line in lines:
    a,b = line.strip().split('-')
#    print (a,b)
    foundA = False
    foundB = False
    nodeA = [a,[]]
    nodeB = [b,[]]
    if pathlist.count(nodeA) == 0:
        pathlist.append(nodeA)
    if pathlist.count(nodeB) == 0:
        pathlist.append(nodeB)

print(pathlist)

for line in lines:
    a,b = line.strip().split('-')
    for x in pathlist:
        node,neighbors = x
        if node == a:
            neighbors.append(b)
        if node == b:
            neighbors.append(a)
print(pathlist)       

print(find_paths([],'start',False))