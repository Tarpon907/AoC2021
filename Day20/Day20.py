from ast import In
import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time

start_time = time.process_time()

# lines = open('c:/users/ted/VSCode/AoC2021/Day20/input1.txt', 'r').readlines()


def read_input():
    with open("c:/users/ted/VSCode/AoC2021/Day20/input1.txt", 'r') as file:
        input = file.read()

    global algo_str, raw_image_data
    algo_str = input.split("\n\n")[0]
    raw_image_data = input.split("\n\n")[1].split("\n")
    raw_image_data.pop()

    image_width = len(raw_image_data[0])
    image_height = len(raw_image_data)
#    print(image_width,image_height)
#    print(image_data[image_height-1])
    #print(algo_str)
    return 

def print_image(input_image):
    for x in input_image:
        print (x)

def magnify_image(old_image,image_width,image_height):

    new_image = []

    for y_index in range(image_height):
        in_line = old_image[y_index]
        new_line = ""
        for x_index in range(image_width):
            val = 0
            for y in range(-1,2):
  #              print("")
                for x in range(-1,2):
                    val = val * 2
                    if y_index + y >= 0 and y_index + y < image_height and x_index + x >= 0 and x_index + x < image_width:
                        in_char = old_image[y_index+y][x_index+x]
                    else:
                        in_char = old_image[y_index][x_index]
   #                 print(in_char,end='')
                    if in_char == '#':
                        val = val + 1
    #        print(val)
            new_line = new_line + algo_str[val]
    #        print("")
        new_image.append(new_line)
                
#    print_image(new_image)
    return new_image

def count_lights(image):
    count = 0

    for y in image:
        for x in range(len(y)):
            if y[x] == '#':
                count = count + 1

    return count


def expand_image(input_image, iteration):
    width = len(input_image[0])
    height = len(input_image)
    new_width = width+2
    new_height = height+2
    pad_char = '.' if iteration % 2 == 0 else '#'
    blank_string = "".ljust(new_width,pad_char)
 #   blank_string.ljust(new_width,'.')
    new_image = [blank_string]
    for x in range(height):
        new_image.append(pad_char + input_image[x] + pad_char)
    new_image.append(blank_string)
#    print_image(new_image)
    return new_image

read_input()
print(algo_str)
print_image(raw_image_data)

current_image = raw_image_data
iterations = 50

for x in range(iterations):
    foo = expand_image(current_image,x)
    current_image = magnify_image(foo,len(foo[0]),len(foo))
    print(count_lights(current_image))


#print_image(current_image)
print(count_lights(current_image))


