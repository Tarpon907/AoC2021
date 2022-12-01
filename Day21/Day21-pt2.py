
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
roll_distribution = [[3,1],[9,1],[4,3],[8,3],[5,6],[7,6],[6,7]]

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

def roll_die_100():
    global last_roll, roll_count
    last_roll = last_roll % 100 + 1
    roll_count = roll_count + 1
    return last_roll

def winner_found(player_data):
    for player in player_data:
        if player[1] >= 21:
            return True
    return False


read_input()
win_count = [0,0]

def quantum_die(roll, old_player_data, whose_turn,level):
    global roll_distribution
    player_data = old_player_data.copy()
    [position,score] = player_data[whose_turn]
    position = (position + roll) % 10
    score = score + position + 1
    player_data[whose_turn] = [position,score]
    win = [0,0]
    indent = "".ljust(level*4," ")
    #print(indent,roll,"||",player_data)
    if winner_found(player_data):
        win[whose_turn] = 1
        return win
    else:
        other_player = (whose_turn + 1) % 2
        for next_roll in roll_distribution:
            result = quantum_die(next_roll[0],player_data,other_player,level+1)
            for i in range(2):
                win[i] = win[i] + result[i] * next_roll[1]
        return win
    

for next_roll in roll_distribution:
    result = quantum_die(next_roll[0],player_data,0,0)
    for i in range(2):
        win_count[i] = win_count[i] + result[i] * next_roll[1]

print(win_count)
if win_count[0] > win_count[1]:
    print(win_count[0])
else:
    print(win_count[1])
    




print("execution time (in ms): ",(time.process_time()-start_time)*1000) 
