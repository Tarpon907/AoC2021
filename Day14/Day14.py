import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time

start_time = time.time()

from string import ascii_uppercase

lines = open('c:/users/ted/AoC/AoC2021/Day14/sample.txt', 'r').readlines()

polymer = lines[0].strip()

rules = []
for line in lines:
    if line.find('-') == -1:
        continue

    pattern, insertion = line.strip().split(" -> ")
    rules.append([pattern,insertion])

print (polymer)
print (rules)

for i in range(20):
    newstring = ""
    for j in range(len(polymer)):
        begin = polymer[j:j+2]
        if len(begin) == 1:
            newstring += begin
            continue
 #       print("searching for: ", begin)
        found = False
        rule = []
        k = 0
        while k < len(rules) and not found:
            if rules[k][0] == begin:
                found = True
                rule = rules[k]
#                print("found ",rule)
            k += 1
        if not found:
            newstring += begin[0]
        else:
            newstring += begin[0]+rule[1]
 #   print(newstring)
    polymer = newstring

counter = []
for letter in ascii_uppercase:
    counter.append(polymer.count(letter))

while counter.count(0) > 0:
    counter.remove(0)
print(counter)

max_count = counter[0]
min_count = counter[0]

for number in counter:
    max_count = max(max_count,number)
    min_count = min(min_count,number)

print(max_count - min_count)

        

print("execution time: ",(time.time()-start_time)*1000)