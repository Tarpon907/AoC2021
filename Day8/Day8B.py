import scipy as sp
import matplotlib.pylab as plt
import numpy as np

lines = open('c:/users/ted/AoC/Day8/input.txt', 'r').readlines()

def decode_usp(usp):
    numberstring = [''] * 10
    segment = [''] * 7
    # first find the 1, 4, 7, 8
    for thisusp in usp:
        if len(thisusp) == 2:
            numberstring[1] = thisusp
        elif len(thisusp) == 4:
            numberstring[4] = thisusp
        elif len(thisusp) == 3:
            numberstring[7] = thisusp
        elif len(thisusp) == 7:
            numberstring[8] = thisusp

    # we can get segment 0 from the difference between 7 and 1   
    for char in numberstring[7]:
        if numberstring[1].find(char) == -1:
            segment[0] = char
            break

    #we need the segments that are distinct between 6 segment numbers
    sixsegments = []
    for char in ('abcdefg'):
        for thisusp in usp:
            if len(thisusp) != 6:
                continue
            if thisusp.find(char) == -1:
                sixsegments.append(char)
    print(sixsegments)

    # now find the sixsegment that isn't in 1
    for char in sixsegments:
        abort = 0
        if numberstring[1].find(char) != -1:
            segment[2] = char
            for thisusp in usp:
                if len(thisusp) != 6:
                    continue
                if thisusp.find(char) == -1:
                    numberstring[6] = thisusp
                    print(sixsegments)
                    print(char)
                    sixsegments.remove(char)
                    abort = 1
                    break
        if abort == 1:
            break
    print("sixsegments:")
    print(sixsegments)
    print(numberstring)        

    # Now we need the five segment number without segment 2 [5]
    for thisusp in usp:
        if len(thisusp) != 5:
            continue
        # Segment 2 missing means it's a 5
        if thisusp.find(segment[2]) == -1:
            numberstring[5] = thisusp
            # Now find the other missing segment
            for char in ('abcdefg'):
                if char == segment[2]:
                    continue
                # the other missing segment is segment 4
                if thisusp.find(char) == -1:
                    segment[4] = char
    # and now we can assign the other segment from our 1 string
    for char in (numberstring[1]):
        if char != segment[2]:
            segment[5] = char

    # Now the five segment number without segment 5  [2]
    for thisusp in usp:
        if len(thisusp) != 5:
            continue
        # segment 5 is missing so it a 2.
        if thisusp.find(segment[5]) == -1:
            numberstring[2] = thisusp
            break
 
    # The remining five segment number is 3
    for thisusp in usp:
        if len(thisusp) != 5:
            continue
        if numberstring.count(thisusp) == 0:
            numberstring[3] = thisusp
        # and whatever element of sixsegments is in the 3 is segment 3
        for char in sixsegments:
            if numberstring[3].find(char) != -1:
                segment[3] = char
                break

    # Now whatever is in the 4 that we haven't figured out yet is segment 1
    for char in numberstring[4]:
        if segment.count(char) == 0:
            segment[1] = char
            break    
    
    # whatever character is left is segment 6
    for char in ('abcdefg'):
        if segment.count(char) == 0:
            segment[6] = char
            break

    numberstring[0] = 'abcdefg' 
    numberstring[0] = numberstring[0].replace(segment[3],'')
    numberstring[9] = 'abcdefg'
    numberstring[9] = numberstring[9].replace(segment[4],'')

    print(numberstring)        
    print(segment)               

    for i in range(10):
        sortedchars = sorted(numberstring[i])
        numberstring[i] = "".join(sortedchars)

    returnval = [segment,numberstring]

    return returnval



total = 0   
for line in lines:
    uspraw, fdovraw = line.split('|')
    usp = uspraw.strip().split(' ')
    fdov = fdovraw.strip().split(' ')
    print(usp)
    print(fdov)
    segments, numberstrings = decode_usp(usp)
    for i in range(4):
        sortedchars = sorted(fdov[i])
        fdov[i] = "".join(sortedchars)

    value = 0
    for thisfdov in fdov:
        value *= 10
        fdov_value = numberstrings.index(thisfdov)
        print(fdov_value)
        value += fdov_value

    print(value)
    total += value

print(total)

