import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time

start_time = time.process_time()

lines = open('c:/users/ted/VSCode/AoC2021/Day18/input.txt', 'r').readlines()

class Node:

    def insert_left(self,input_line,index):
#        print("inserting left at", input_line[index])
        self.left = Node()
        self.left.parent = self
        index = self.left.process(input_line,index)
        return index

    def insert_right(self,input_line,index):
        self.right = Node()
        self.right.parent = self
        index = self.right.process(input_line,index)
        return index

    def set_left(self,left):
        self.left = left
        return self
    
    def set_right(self,right):
        self.right = right
        return self

    def set_parent(self,parent):
        self.parent = parent
        return self

    def update_data(self,data = None):
        self.data = data
        return self

    def update_left(self,data = None):
        if self.left:
            self.left.data = data
        return self

    def update_right(self,data = None):
        if self.right:
            self.right.data = data
        return self

    def get_tree_string(self,isRoot = True,wholeTree = False):
        tree = self
        if wholeTree:
            while tree.parent is not None:
                tree = tree.parent
        tree_string = ""
        if tree.left:
            tree_string += "["
            tree_string += tree.left.get_tree_string(False)
            tree_string += ","       
            tree_string += tree.right.get_tree_string(False)
            tree_string += "]"
        elif tree.data is not None:
            tree_string += str(tree.data)
        return tree_string      

    def PrintTree(self,isRoot = True):

        print(self.get_tree_string(isRoot))


    def find_explode(self,level):
        # so when do we explode?  When level  >= 5 and children have data
#        print("at level", level,"looking at subtree: ",self.get_tree_string())
        if level >= 5 and self.data is not None:
            return False
        if level >= 5 and self.left.data is not None and self.right.data is not None:
            pre_explosion = self.get_tree_string()
 #           print("Need to explode:", pre_explosion)
            self.explode_node()
            post_explosion = self.get_tree_string()
 #           print("exploded:",pre_explosion)
 #           print("and got :",post_explosion)
            return True
        elif self.data:
            return False
        elif self.left and self.left.find_explode(level+1):
            return True
        elif self.right and self.right.find_explode(level+1):
            return True
        return False

    def explode_node(self):
        pre_explosion = self.get_tree_string()
#        print("exploding:",pre_explosion)
        left_neighbor = self.find_left_neighbor()
        right_neighbor = self.find_right_neighbor()
        if left_neighbor:
#            print("left neighbor:",left_neighbor.data)
            left_neighbor.data += self.left.data
#        else:
#            print ("no left neighbor")
        if right_neighbor:
#            print("right neighbor:",right_neighbor.data)
            right_neighbor.data += self.right.data
#        else:
#            print ("no right neighbor")
        self.set_left(None).set_right(None).update_data(int(0))
#        print("after explosion:", self.parent.get_tree_string(wholeTree=True))
    
    def find_left_neighbor(self):
#        print("find_left_neighbor")
        # NEed to go up until you can go down to the left once, then down to the right.

        # we are starting at the parent of the data nodes themselves.  So, that's self.
        
        previous_node = self
        current_node = self.parent

        while current_node.left == previous_node and current_node.parent is not None:
            previous_node = current_node
            current_node = current_node.parent

        if current_node.left == previous_node:
            #got to the top of the tree, but still can't go left, so there is no left neighbor
            return None
        # So now we can go down one to the left
        current_node = current_node.left
        # and then down to the right until we get to data
        while current_node.right is not None:
            current_node = current_node.right
#        if current_node is not None:
#            print("left neighbor:", current_node.data)
        return current_node

    def find_right_neighbor(self):
#        print("find_right_neighbor")
        # NEed to go up until you can go down to the right once, then down to the left.
        # we are starting at the parent of the data nodes themselves.  So, that's self.
        
        previous_node = self
        current_node = self.parent


        while current_node.right == previous_node and current_node.parent is not None:
#            current_node.PrintTree()
            previous_node = current_node
            current_node = current_node.parent

        if current_node.right == previous_node:
            #got to the top of the tree, but still can't go right, so there is no right neighbor
            return None
        # So now we can go down one to the rightz
        current_node = current_node.right
        # and then down to the left until we get to data
        while current_node.left is not None:
            current_node = current_node.left
#        if current_node:
#            print("right neighbor:", current_node.data)
        return current_node
   
        

        



    def __init__(self, data = None, parent = None):
#        print("creating node")
        self.left = None
        self.right = None
        self.data = data
        self.parent = parent



    def snailfish_add(self, subtree):
#        print("adding", self.get_tree_string(), "and", subtree.get_tree_string())
        newtree = Node()
        newtree.set_left(self)
        self.set_parent(newtree)
        newtree.set_right(subtree)
        subtree.set_parent(newtree)

#        newtree.PrintTree()

        level = 1
        
        new_split = True
        while new_split:
            new_split = False
            exploded = True
            while exploded:
                exploded = False
                exploded = newtree.find_explode(level)
#                print("after explosion:",newtree.get_tree_string())

            new_split = newtree.find_split()
#            print("after split:", newtree.get_tree_string())

#        print("result of add:",newtree.get_tree_string())

        return newtree
        

    def find_split(self):
        found_split = False
#        print("looking for split")
#        print(self.data) if self.data is not None else self.PrintTree()
        if self.left is not None:
            found_split = self.left.find_split()
            if found_split:
                return True
        if self.right is not None:
            found_split = self.right.find_split()
            if found_split:
                return True
        if self.data is not None and self.data > 9:
#            print("found split", self.data)
            left_data = int(self.data/2)
            right_data = self.data - left_data
            self.left = Node(data = left_data, parent = self)
            self.right = Node(data = right_data, parent = self)
            self.data = None
#            print("split into:",self.get_tree_string())
#            print(self.get_tree_string(wholeTree=True))
            return True
        else:
            return False

        




    def process(self, input_line, index = 0):
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
        
       
    def find_magnitude(self):
        if self.data is not None:
            return self.data
        return 3 * self.left.find_magnitude() + 2 * self.right.find_magnitude()


max_mag = 0
for i in range(len(lines)-1):
    for j in range(i+1,len(lines)):
#        print(i,j)
        tree = Node()
        tree.process(lines[i].strip())
#        tree.PrintTree()
        subtree = Node()
        subtree.process(lines[j].strip())
#        subtree.PrintTree()
        tree = tree.snailfish_add(subtree)
        mag1 = tree.find_magnitude()

        tree = Node()
        tree.process(lines[j].strip())
#        tree.PrintTree()
        subtree = Node()
        subtree.process(lines[i].strip())
#        subtree.PrintTree()
        tree = tree.snailfish_add(subtree)
        mag2 = tree.find_magnitude()
        max_mag = max(max_mag,mag1)
        max_mag = max(max_mag,mag2)

        print(i,j,"|mag1, mag2, max:",mag1,mag2,max_mag)       
    




    




print("execution time (in ms): ",(time.process_time()-start_time)*1000) 