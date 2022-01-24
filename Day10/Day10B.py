import scipy as sp
import matplotlib.pylab as plt
import numpy as np

lines = open('c:/users/ted/AoC/AoC2021/Day10/input.txt', 'r').readlines()

opens = '([{<'
closes = ')]}>'
#scores = [3,57,1197,25137]
scores = [1,2,3,4]


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
                print("score:", 0)
                return 0
        x += 1
    if len(stack) != 0:
        score = 0
        for remaining in stack:
            index = opens.find(remaining)
            score = score*5 + scores[index]
            print(score, end=" ")
        print(score,": ", stack)
        return score 


            


results = []
for line in lines:
    result = process_line(line.strip())
    if result != 0:
        results.append(result)

results.sort()
print(results)
index = int((len(results)-1)/2)
print (index)
answer = results[index]
print(answer)


