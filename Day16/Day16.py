import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time

start_time = time.process_time()

lines = open('c:/users/ted/AoC2021/Day16/sample.txt', 'r').readlines()




line = lines[0].strip()
binary_line = ""

print(line)
for char in line:
    print(str(bin(int(char,base=16)))[2:].zfill(4))
    binary_line += str(bin(int(char,base=16)))[2:].zfill(4)




print(binary_line)

index = 0
packet_length = 0
while index < len(binary_line):
    packet_start = index
    packet_version = int(binary_line[index:index+3],base=2)
    index += 3
    print ("version:", packet_version)
    packet_type = int(binary_line[index:index+3],base=2)
    index += 3
    print ("type", packet_type)
    if packet_type == 4:
        temp_index = packet_start
        last_chunk= False
        literal_string = ""
        while not last_chunk:
            chunk = binary_line[index:index+5]
            if chunk[0] == '0':
                last_chunk = True
            literal_string += binary_line[index+1:index+5]
            index += 5
        while temp_index < index:
            temp_index += 4
        print("index, temp_index", index, temp_index)
        print(temp_index - index)
        print(literal_string)
        print(int(literal_string,base=2))
    
        
            

    exit()












print("execution time (in ms): ",(time.process_time()-start_time)*1000) 