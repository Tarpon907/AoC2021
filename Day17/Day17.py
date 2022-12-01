import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time

start_time = time.process_time()

target_min_x = 20
target_max_x = 30
target_min_y = -10
target_max_y = -5
target_min_x = 257
target_max_x = 286
target_min_y = -101
target_max_y = -57

possible_Vx = []
for start_x in range(target_max_x,target_min_x-1,-1):

    x = start_x
    steps = 0
    while x > 0:
        steps += 1
        x -= steps
    if x == 0:
#        print(steps, "steps to ", start_x)
        possible_Vx.append(steps)
#print (possible_Vx)

maxmax = 0
maxmaxes = []
hitcount = 0
points = []
tries = 0
for x0 in range(min(possible_Vx),target_max_x+1):
    for y0 in range(target_min_y,1000):
 #       print ("trying", x0,y0)
        tries += 1
        xpos = ypos = 0
        Vy = y0
        Vx = x0
        hit = False
 #       print(Vx,Vy,xpos,ypos)
        while ypos >= target_min_y and xpos <= target_max_x:
            if xpos >= target_min_x and xpos <= target_max_x and ypos >= target_min_y and ypos <= target_max_y:
                hit = True
                points.append([x0,y0])
                break            
            ypos = ypos + Vy
            xpos = xpos + Vx
            if Vx > 0:
                Vx -= 1
            Vy -= 1
 #           print("[",Vx,Vy,"]","(",xpos,ypos,")")


        if hit:
            hitcount += 1
 #           print("[",x0,y0,"]","(",xpos,ypos,")")


points.sort()
for i in points:
    print(i)
print("hits:", hitcount)
print("tries:", tries)

    
        



print("execution time (in ms): ",(time.process_time()-start_time)*1000) 