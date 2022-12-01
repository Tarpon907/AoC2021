import scipy as sp
from mpl_toolkits import mplot3d
import matplotlib.pylab as plt
import numpy as np
import re
import time
import logging
import collections

start_time = time.process_time()



def read_input():
    global player_data
    with open("c:/users/ted/VSCode/AoC2021/Day22/input1.txt", 'r') as file:
        input = file.read()


