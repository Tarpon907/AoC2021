import scipy as sp
import matplotlib.pylab as plt
import numpy as np

lines = open('c:/users/ted/AoC/AoC2021/Day12/input.txt', 'r').readlines()

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self,node):
        node.next = self.head
        self.head = node


class Node:
    def __init__(self,data):
        self.data = data
        self.large = False
        self.next = None
        self.neighbors = []
        if data[0].isupper():
            self.large = True
        

    def __repr__(self):
        nodestring = []
        nodestring.append(self.data)
 #       nodestring.append(str(self.large))
 #       for x in self.neighbors:
 #           nodestring.append(x.data)
        return " - ".join(nodestring)

    def add_neighbor(self,node):
        self.neighbors.append(node)

def find_path(current_path,room):
    print(current_path, " -> ", room.data)
    if room.data == "end":
        current_path.append(room.data)
        print("good path: ",current_path)
        current_path.pop()
        return 1
    if room.data == "start" and len(current_path) > 0:
        return 0
    if room.data.islower():
 #       print(room.data, current_path)
        if current_path.count(room.data) > 0:
            return 0
    current_path.append(room.data)
    retval = 0
    neighbors = room.neighbors.copy()
    print(room.data, " neighbors: ",neighbors)
    for next_room in neighbors:
        print("next room: ", next_room)
        retval += find_path(current_path,next_room)
    current_path.pop()
    return retval

# first lets find all the rooms and make a list of them
startnode = None
rooms = LinkedList()
for line in lines:
    a,b = line.strip().split('-')
#    print (a,b)
    foundA = False
    foundB = False
    for node in rooms:
        if node.data == a:
            foundA = True
        if node.data == b:
            foundB = True
    if not foundA:
        rooms.add_first(Node(a))
    if not foundB:
        rooms.add_first(Node(b))
    print(rooms)

# now we go through again and establish neighbors
for line in lines:
    a,b = line.strip().split('-')
#    print (a,b)
    nodeA = None
    nodeB = None
    for node in rooms:
        if node.data == a:
            nodeA = node
        if node.data == b:
            nodeB = node
    nodeA.add_neighbor(nodeB)
    nodeB.add_neighbor(nodeA)
    if startnode == None:
        if a == "start":
            startnode = nodeA
        if b == "start":
            startnode = nodeB
#    print(nodeA)
#    print(nodeB)

for node in rooms:
    print(node)

print("start node:", startnode)

my_path = []
print(find_path(my_path,startnode))


        


