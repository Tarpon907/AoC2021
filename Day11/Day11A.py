import scipy as sp
import matplotlib.pylab as plt
import numpy as np

lines = open('c:/users/ted/AoC/AoC2021/Day11/input.txt', 'r').readlines()

startgrid = np.ndarray((10,10),dtype=int)
untouchedflash = np.ndarray((10,10),dtype=bool)

i = 0
for line in lines:
    for j in range(10):
        startgrid[i][j] = int(line[j])
        untouchedflash[i][j] = False
    i += 1


def cascade(i, j, grid, flashed):

    if flashed[i][j]:
        return
    grid[i][j] = grid[i][j] + 1
    return


def age_grid(grid):
    count = 0
    flashed = np.copy(untouchedflash)
    newgrid = np.copy(grid)
    for i in range(10):
        for j in range(10):
            newgrid[i][j] += 1

    newflash = True
    while newflash:
        newflash = False
        newgrid2 = np.copy(newgrid)
 #       print("process this:\n",newgrid2)
        for i in range(10):
            for j in range(10):
                if newgrid[i][j] > 9:
                    if flashed[i][j]:
                        continue
                    flashed[i][j] = True
                    newflash = True
 #                   print("Flash at ","[",i,",",j,"]")
                    for a in range(i-1,i+2):
                        for b in range(j-1,j+2):
                            if a < 0 or b < 0 or a > 9 or b > 9 or (a == i and b == j):
                                continue
                            if flashed[a][b]:
 #                               print("[",a,",",b,"] already flashed")
                                continue
 #                           print("[",a,",",b,"]")
                            newgrid2[a][b] += 1

        newgrid = np.copy(newgrid2)
 #       print(newgrid)

    for i in range(10):
        for j in range(10):
            if newgrid[i][j] > 9:
                count += 1
                newgrid[i][j] = 0
            
 #   print(newgrid)
    return newgrid, count
 
print(startgrid)
total = 0
nextgrid = np.copy(startgrid)
day = 1
while True:
    grid, count = age_grid(nextgrid)
    nextgrid = np.copy(grid)
    total += count
    print ("\n ---->", nextgrid)
    if count == 100:
        print(day)
        exit()
    day += 1
