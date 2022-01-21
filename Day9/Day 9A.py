import scipy as sp
import matplotlib.pylab as plt
import numpy as np

lines = open('c:/users/ted/AoC/Day 9/input.txt', 'r').readlines()

width = len(lines[0]) - 1
height = len(lines)


lava = np.ndarray((height+2, width+2),dtype=int)

for i in range(height+2):
    lava[i][0] = 9
    lava[i][width+1] = 9
for j in range(width+2):
    lava[0][j] = 9
    lava[height+1][j] = 9

i = 1
for line in lines:
    j = 1
    for char in line.strip():
        lava[i][j] = int(char)
        j += 1
    i += 1

print(lava)

lowpoints = []
totalrisk = 0
for i in range(height):
    for j in range(width):
        y = i + 1
        x = j + 1
        risk = 0
        if lava[y][x] >= lava[y-1][x]:
            continue
        if lava[y][x] >= lava[y+1][x]:
            continue
        if lava[y][x] >= lava[y][x-1]:
            continue
        if lava[y][x] >= lava[y][x+1]:
            continue
        
        risk = lava[y][x] + 1
        lowpoints.append([y,x])
        print(risk)
        totalrisk += risk

print(totalrisk)
print (lowpoints)