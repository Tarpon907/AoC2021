
lines = open("c:/users/ted/aoc/day 6/input.txt", 'r').readlines()

input = lines[0].rstrip().split(',');
print(input)

fishes = [0] * 9

for fish in input:
    fishes[int(fish)] += 1

for x in range(257):
    print("Day ", x, end=': ')
    print(fishes, end = ' ')
    total = 0
    for i in range(9):
        total = total + fishes[i]
    print(total)
    new8 = fishes[0]
    new6 = fishes[0]
    for i in range(8):
        fishes[i] = fishes[i+1]
    fishes[6] += new6
    fishes[8] = new8

