import math
import re

part_1 = False
file = '../input.txt'

if part_1:
    races = [list(map(int, re.findall(r'\d+', line))) for line in open(file).readlines()]
else:
    races = [[int(''.join(re.findall(r'\d+', line)))] for line in open(file).readlines()]

result = 1
for time, distance in zip(*races):

    low = math.ceil((time - math.sqrt(time**2 - 4*distance)) / 2)
    if low**2 - time*low == -distance:
        low += 1

    high = math.floor((time + math.sqrt(time**2 - 4*distance)) / 2)
    if high**2 - time*high == -distance:
        high -= 1

    if low <= high:
        result *= (high - low + 1)

print(result)