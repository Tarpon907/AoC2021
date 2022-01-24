import scipy as sp
import matplotlib.pylab as plt
import numpy as np

lines = open('c:/users/ted/AoC/AoC2021/Day10/input.txt', 'r').readlines()

opens = '([{<'
closes = ')]}>'
scores = [3,57,1197,25137]

def process_line(line):
    stack = []
 #   print(line, end=" index: ")
    x=0
    for char in line:
 #       print("nextchar: ", char)
        if opens.find(char) != -1:
            stack.insert(0,char)
 #           print("push: ",char,"  ",stack)
        else:
 #           print("closing:",char)
            index = closes.find(char)
            popped = stack.pop(0)
 #           print("pop: ",popped)
 #           print("stack: ", stack)
            if popped != opens[index]:
 #               print ("mismatch", char, popped)
                print("score:", scores[index])
                return scores[index]
        x += 1
    if len(stack) != 0:
 #       print("none - illegal")
        return 0


            


total = 0
for line in lines:
    total += process_line(line.strip())

print("total: ", total)
