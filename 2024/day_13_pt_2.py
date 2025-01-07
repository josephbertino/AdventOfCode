import math
import re
import numpy as np

file = 'input.txt'
prizes = open(file).read().split('\n\n')

pattern = r'(\d+)'
result = 0
for prize in prizes:
    a, b, p = prize.split('\n')
    ax, ay = list(map(int, re.findall(pattern, a)))
    bx, by = list(map(int, re.findall(pattern, b)))
    px, py = list(map(int, re.findall(pattern, p)))
    px, py = px+10000000000000, py+10000000000000

    Amat = [[ax, bx], [ay, by]]
    bmat = [px, py]
    a_sol, b_sol = np.linalg.solve(Amat, bmat)
    a_int, b_int = int(round(a_sol)), int(round(b_sol))
    if a_int >= 0 and b_int >= 0 and a_int*ax + b_int*bx == px and a_int*ay + b_int*by == py:
        result += a_int*3 + b_int

print(result)