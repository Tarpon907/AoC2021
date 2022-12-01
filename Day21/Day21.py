
import scipy as sp
from mpl_toolkits import mplot3d
import matplotlib.pylab as plt
import numpy as np
import re
import time
import logging

start_time = time.process_time()

last_roll = 100
player_data = []
roll_count = 0

def read_input():
    global player_data
    with open("c:/users/ted/VSCode/AoC2021/Day21/input1.txt", 'r') as file:
        input = file.read()

    foo = input.split('\n')
    foo.pop()
    for line in foo:
        print(line)
        line= line.split()
        print(line)
        print(line[1],line[4])
        player_data.append([int(line[4]) - 1,0])

    print(player_data)

def roll_die():
    global last_roll, roll_count
    last_roll = last_roll % 100 + 1
    roll_count = roll_count + 1
    return last_roll

def winner_found():
    global player_data
    for player in player_data:
        if player[1] >= 1000:
            return True
    return False


read_input()

player = 1
while not winner_found():
    player = (player + 1) % 2
    total_roll = roll_die() + roll_die() + roll_die()
    [position,score] = player_data[player]
    position = (position + total_roll) % 10
    score = score + position + 1
    player_data[player] = [position,score]
    print(player_data)

second_place = (player + 1) % 2
print(player_data[second_place][1] * roll_count)



print("execution time (in ms): ",(time.process_time()-start_time)*1000) 
