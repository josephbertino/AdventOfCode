import re
from collections import defaultdict
import string

part1 = False

file = '../input.txt'
roomtags = [re.match(r'(.*)-(\d+)\[(\w+)\]', line.strip()).groups() for line in open(file).readlines()]

def is_real_tag(code, checksum):
    """
    :param str code:
    :param str checksum:
    :return bool:
    """
    counts = defaultdict(int)
    for c in code:
        if c != '-':
            counts[c] += 1
    revcounts = defaultdict(list)
    for k, v in counts.items():
        revcounts[v].append(k)
    mysum = ''.join(l for count, letters in sorted(revcounts.items(), reverse=True) for l in sorted(letters))[:5]
    return checksum == mysum

alphabet = string.ascii_lowercase + string.ascii_lowercase

def shift(char, amt):
    if char == '-':
        return ' '
    amt = amt % 26
    return alphabet[ord(char) - ord('a') + amt]

def is_north_pole_room(code, roomid):
    decoded = ''.join(shift(c, int(roomid)) for c in code)
    return 'north' in decoded and 'pole' in decoded

result = 0
for code, roomid, checksum in roomtags:
    if is_real_tag(code, checksum):
        if part1:
            result += int(roomid)
        elif is_north_pole_room(code, roomid):
            result = int(roomid)
print(result)