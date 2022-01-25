import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time

start_time = time.time()

from string import ascii_uppercase

lines = open('c:/users/ted/AoC2021/Day17/foo.txt', 'r').readlines()

points = []
for line in lines:
    for point in line.strip().split():
        x,y = (point.split(","))
        points.append([int(x),int(y)])
points.sort()
for i in points:
    print(i)
