import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time

start_time = time.time()

lines = open('c:/users/ted/AoC2021/Day15/input.txt', 'r').readlines()

height = len(lines)
width = len(lines[0].strip())

risk = np.ndarray((height,width),dtype=int)
dijkstra = np.full((height,width),fill_value=1000000000000)
minmatrix = np.full((height,width),fill_value=1000000000000)
# unvisited = []
visited = np.full((height,width),fill_value=False)
total_nodes = width * height

for i in range(len(lines)):
    line = lines[i].strip()
    for j in range(len(lines)):
        risk[i][j] = int(line[j])
#        unvisited.append([i,j])
#print (risk)

dijkstra[0][0] = 0

def visit(i,j):
#    print(dijkstra)
#    print("visiting: ",i,j)
    neighbor_risk = [1000000000001] * 4
    neighbor_dir = [[-1,0],[1,0],[0,-1],[0,1]]
    if i > 0:
        neighbor_risk[0] = risk[i-1][j]
    if i < height-1:
        neighbor_risk[1] = risk[i+1][j]
    if j > 0:
        neighbor_risk[2] = risk[i][j-1]
    if j < width-1:
        neighbor_risk[3] = risk[i][j+1]
#    print (neighbor_risk)
   

    while len(neighbor_risk) > 0:
        min_neighbor_risk = min(neighbor_risk)
        if min_neighbor_risk == 1000000000001:
            break
        index = neighbor_risk.index(min_neighbor_risk)
        neighbor_i = i + neighbor_dir[index][0]
        neighbor_j = j + neighbor_dir[index][1]
#        print("checking neighbor at: ",neighbor_i, neighbor_j)
        if not visited[neighbor_i][neighbor_j]:
            dijkstra[neighbor_i][neighbor_j] = min(dijkstra[i][j] + risk[neighbor_i][neighbor_j],dijkstra[neighbor_i][neighbor_j])
            minmatrix[neighbor_i][neighbor_j] = dijkstra[neighbor_i,neighbor_j]
        neighbor_risk.pop(index)
        neighbor_dir.pop(index)
    visited[i][j] = True
#    unvisited.remove([i,j])
    minmatrix[i][j] = 1000000000001;
    return

#print("[0,0]: ", dijkstra[0][0])
visit(0,0)
total_visited = 1
#print("[0,0]: ", dijkstra[0][0])

while total_visited < total_nodes:
    min_i = 0
    min_j = 0
    min_val = 1000000000000
#    for point in unvisited:
#        i, j = point
#        if dijkstra[i][j] < min_val and visited[i][j] == False:
#                min_val = dijkstra[i][j]
#                min_i = i
#                min_j = j
#    print("minmatrix: ", minmatrix)
    index = np.argmin(minmatrix)

    i = int(index / width)
    j = index % width
#    print("argmin index:", index, "coirelates to: ", i, j)
    visit(i, j)
    total_visited += 1
    if dijkstra[0][0] != 0:
        print (dijkstra)
        print ("visiting: ",i,j)

print(dijkstra[height-1,width-1])








    
    



print("execution time (in ms): ",(time.time()-start_time)*1000) 
