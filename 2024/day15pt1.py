file = '../input.txt'

'''
test final

########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########
'''

DIRS = {'<':(0,-1), '>':(0,1), 'v':(1,0), '^':(-1,0)}
BOX = 'O'
ROBOT = '@'
WALL = '#'
EMPTY = '.'

floor = [list(line.strip()) for line in open(file).readlines() if line.startswith('#')]
steps = ''.join([line.strip() for line in open(file).readlines() if line[0] in '<>^v'])


def print_floor():
    print()
    for line in floor:
        print(''.join(line))
    print()


def push_boxes(pos, step):
    """
    Determine if we can push the boxes from <pos> in <direction>.
        If not, return False.
        Otherwise, push boxes, freeing up space, and return True
    :param (int, int) pos:
    :param str step:
    :return bool:
    """
    r, c = pos
    dr, dc = DIRS[step]
    pos_obj = floor[r][c]
    while pos_obj == BOX:
        r += dr
        c += dc
        pos_obj = floor[r][c]
    if pos_obj == WALL:
        return False
    else:
        floor[r][c] = BOX
        floor[pos[0]][pos[1]] = EMPTY
        return True


def move(pos, step):
    """
    :param (int, int) pos:
    :param str step:
    :return (int, int):
    """
    r, c = pos
    dr, dc = DIRS[step]
    next_r, next_c = r + dr, c + dc
    next_pos = floor[next_r][next_c]
    if (next_pos == WALL) or (next_pos == BOX and not push_boxes((next_r, next_c), step)):
        return pos
    else:
        floor[next_r][next_c] = ROBOT
        floor[r][c] = EMPTY
        return next_r, next_c


pos = [(r, c) for c, line in enumerate(floor) for r, char in enumerate(line) if char == '@'][0]
for step in steps:
    pos = move(pos, step)


gps = 0
for r, line in enumerate(floor):
    for c, char in enumerate(line):
        if char == BOX:
            gps += (100*r) + (c)

print(gps)