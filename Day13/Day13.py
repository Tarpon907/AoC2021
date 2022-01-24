import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re

lines = open('c:/users/ted/AoC/AoC2021/Day13/input.txt', 'r').readlines()

points = []
fold = []
p = re.compile('(\w)=(\d+)')
for line in lines:
    if line.find(',') != -1:
        x,y = line.strip().split(',')
        points.append([int(x),int(y)])
    if line.find('=') != -1:
        m = p.search(line.strip())
        fold.append([m.group(1),int(m.group(2))])

print(points)
print(fold)

for i in fold:
    axis = i[0]
    value = i[1]

    if axis == 'y':
        for j in range(len(points)):
            if points[j][1] > value:
                points[j][1] -= (points[j][1] - value) * 2
    else:
        for j in range(len(points)):
            if points[j][0] > value:
                points[j][0] -= (points[j][0] - value) * 2

    points.sort()
    max_x = 0
    max_y = 0
    for point in points:
        max_x = max(max_x,point[0])
        max_y = max(max_y,point[1])
        while points.count(point) > 1:
            points.remove(point)
    print(len(points), max_x, max_y)

print(points)
string = "".ljust(max_x+1)
display = [string] * (max_y+1)
for point in points:
    string = display[point[1]]
    position = point[0]
    string = string[:position] + '#' + string[position+1:]
    display[point[1]] = string
for i in range(len(display)):
    print(display[i])





