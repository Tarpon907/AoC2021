import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time

start_time = time.time()

from string import ascii_uppercase

lines = open('c:/users/ted/AoC/AoC2021/Day14/input.txt', 'r').readlines()

polymer = lines[0].strip()

rules = []
for line in lines:
    if line.find('-') == -1:
        continue

    pattern, insertion = line.strip().split(" -> ")
    rules.append([pattern,insertion])

print (polymer)
print (rules)

combolist = []
combocount = []

for i in range(len(polymer)-1):
    pair = polymer[i:i+2]
    if len(pair) < 2:
        continue
    print(pair)
    combolist.append(pair)
    combocount.append(1)
print(combolist)
print(combocount)

for i in range(40):
    newcombolist = combolist.copy()
    newcombocount = combocount.copy()

    for index in range(len(combolist)):
        combo = combolist[index]
        found = False
        for newindex in range(len(newcombolist)):
            if newcombolist[newindex] == combo:
                found = True
                break
        newcombocount[newindex] -= combocount[index]

        rule = []
        found = False
        for rule in rules:
            if rule[0] == combo:
                found = True
                break
#               print("found ",rule)
        print(found, combo, rule)
        newpairs = [combo[0] + rule[1], rule[1] + combo[1]]

        for j in range(2):
            found = False
            for newindex in range(len(newcombolist)):
                if newcombolist[newindex] == newpairs[j]:
                    found = True
                    break
            if not found:
                newcombolist.append(newpairs[j])
                newcombocount.append(combocount[index])
            else:
                newcombocount[newindex] += combocount[index];
    print (newcombolist)
    print (newcombocount)
    combolist = newcombolist
    combocount = newcombocount

counter = []
for letter in ascii_uppercase:
    counter.append(0)

counter[ascii_uppercase.find(polymer[0])-ascii_uppercase.find('A')] += 1
counter[ascii_uppercase.find(polymer[len(polymer)-1])-ascii_uppercase.find('A')] += 1

i = 0
for i in range(len(combolist)):
    pair = combolist[i]
    counter[ascii_uppercase.find(pair[0])-ascii_uppercase.find('A')] += combocount[i]
    counter[ascii_uppercase.find(pair[1])-ascii_uppercase.find('A')] += combocount[i]

while counter.count(0) > 0:
    counter.remove(0)

max_count = counter[0]/2
min_count = max_count
for i in counter:
    i /= 2
    max_count = max(max_count, i)
    min_count = min(min_count, i)

print(max_count - min_count)       



print("execution time (in ms): ",(time.time()-start_time)*1000)        

            
           


