import scipy as sp
import matplotlib.pylab as plt
import numpy as np

lines = open('c:/users/ted/AoC/Day8/input.txt', 'r').readlines()

count = 0
for line in lines:
    uspraw, fdovraw = line.split('|')
    usp = uspraw.strip().split(' ')
    fdov = fdovraw.strip().split(' ')
    print(usp)
    print(fdov)
    for ov in fdov:
        if len(ov) <5 or len(ov) == 7:
            count += 1

print(count)
