import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time

start_time = time.process_time()

lines = open('c:/users/ted/AoC2021/Day18/sample.txt', 'r').readlines()

class Node:

    def insert_left(self,input_line,index):
#        print("inserting left at", input_line[index])
        self.left = Node(self)
        index = self.left.process(input_line,index)
        return index

    def insert_right(self,input_line,index):
        self.right = Node(self)
        index = self.right.process(input_line,index)
        return index

    def set_left(left):
        self.left = left
        return
    
    def set_right(right):
        self.right = right
        return

    def set_parent(parent):
        self.parent = parent
        return

    def update_data(self,data = None):
        if self.right:
            self.data = data

    def update_left(self,data = None):
        if self.left:
            self.left.data = data

    def update_right(self,data = None):
        if self.right:
            self.right.data = data

    def PrintTree(self,isRoot = True):
        if self.left:
            print("[",end="")
            self.left.PrintTree(False)
            print(",",end="")            
            self.right.PrintTree(False)
            print("]",end="")
        elif self.data:
            print(self.data,end="")

        if isRoot:
            print()

    def find_explode(self,level):
        # so when do we explode?
        
        if not self.data:
            
        if self.data and level < 5:
            return False
        if self.left.data and self.right.data:

        



    def __init__(self, data = None, parent = None):
#        print("creating node")
        self.left = None
        self.right = None
        self.data = data
        self.parent = parent

    def snailfish_add(self, subtree):
        newtree = Node()
        newtree.set_left(self)
        self.set_parent(newtree)
        newtree.set_right(subtree)
        subtree.set_parent(newtree)

        level = 1
        
        new_split = True
        while new_split:
            new_split = False
            exploded = True
            while exploded:
                exploded = False
                exploded = newtree.find_explode(level)
            new_split = newtree.find_split()
        




    def process(self, input_line, index):
#        print(input_line[index:])
        while (index < len(input_line)):
            if input_line[index] == '[':
#                print("[: process_left:",input_line[index+1:])
                index = self.insert_left(input_line,index+1)
            elif input_line[index] == ',':
#                print(",: process_right:",input_line[index+1:])
                index = self.insert_right(input_line,index+1)
            elif input_line[index] == ']':
#                print("]: return to parent")          
                return index + 1
            else:
#                print("data: add and return:",input_line[index+1:])
                self.data = int(input_line[index])
                return index + 1
        
       
    


tree = Node()
index = tree.process(lines[0].strip(),0)
tree.PrintTree()
for line in lines[1:]:
    subtree = Node()
    index = tree.process(line.strip(),0)

    tree.snailfish_add(subtree)
    
    tree.PrintTree()
    




print("execution time (in ms): ",(time.process_time()-start_time)*1000) 