import scipy as sp
import matplotlib.pylab as plt
import numpy as np

lines = open('c:/users/ted/AoC/Day7/input.txt', 'r').readlines()

positions = lines[0].rstrip().split(",")

maxpos = 0
for i in range(len(positions)):
    maxpos = max(maxpos,int(positions[i]))

total = [0] * (maxpos+1)
for i in range(maxpos+1):
    for j in positions:
        distance = abs(int(j)-i) * 1.0
        fuel = distance * (distance + 1) / 2.0
        total[i] += fuel

print(total)
print(total.index(min(total)))
print(min(total))

t = sp.linspace(0,maxpos,maxpos+1)
totalarray = np.array(total)[t.astype(int)]
plt.plot(t,totalarray)
plt.show()
