import re
from math import lcm

part_1 = False
file = '../input.txt'

instructions = open(file).read().split('\n')
directions = instructions[0].strip()
node_map = {}
for d in instructions[2:]:
    match = re.match(r'(\w{3}) = \((\w{3}), (\w{3})\)', d)
    source, left, right = match.groups()
    node_map[source] = (left, right)

dirs = {'L': 0, 'R': 1}
N = len(directions)

def get_next_turn():
    i = 0
    while True:
        yield dirs[directions[i % N]]
        i += 1


if part_1:
    starts = ['AAA']
else:
    starts = [k for k in node_map.keys() if k.endswith('A')]

print(starts)

scores = []
for start in starts:
    turn_gen = get_next_turn()
    num_moves = 0
    while True:
        num_moves += 1
        turn_idx = next(turn_gen)
        start = node_map[start][turn_idx]
        if start.endswith('Z'):
            break
    scores.append(num_moves)

result = lcm(*scores)
print(result)
