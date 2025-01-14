import re
from functools import reduce

part_1 = False

FLOOR_W = 101
FLOOR_H = 103
COUNT = 100
quad_scores = [0] * 4

file = '../input.txt'
trajs = [tuple(map(int, re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line).groups())) for line in open(file).readlines()]
positions = [(x, y) for x, y, dx, dy in trajs]
velocities = [(dx, dy) for x, y, dx, dy in trajs]

def mult(x, y):
    return x * y

def get_quad_index(x, y):
    a = 0 if x < FLOOR_W // 2 else 1
    b = 0 if y < FLOOR_H // 2 else 2
    return a + b

def print_floor(positions):
    floor = [['_'] * FLOOR_W for _ in range(FLOOR_H)]
    for x, y in positions:
        floor[y][x] = 'X'
    for row in floor:
        print(''.join(row))
    print('\n\n')


if part_1:
    for x, y, dx, dy in trajs:
        final_x = (x + (COUNT * dx)) % FLOOR_W
        final_y = (y + (COUNT * dy)) % FLOOR_H
        if final_x == (FLOOR_W // 2) or final_y == (FLOOR_H // 2):
            continue
        quad_scores[get_quad_index(final_x, final_y)] += 1
    print(quad_scores)
    result = reduce(mult, quad_scores)
    print(result)
else:
    for i in range(FLOOR_H * FLOOR_W):
        new_pos = [((x+dx) % FLOOR_W, (y+dy) % FLOOR_H) for (x, y), (dx, dy) in zip(positions, velocities)]
        if len(new_pos) == len(set(new_pos)):
            print(i + 1)
            print_floor(new_pos)
            break
        positions = new_pos