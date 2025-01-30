import re

part1 = False
file = '../input.txt'

def is_valid_ip_pt_1(i, s):
    bad_pattern = r'\[\w*([a-z])(?!\1)([a-z])\2\1\w*\]'
    good_pattern = r'([a-z])(?!\1)([a-z])\2\1'
    flag = re.search(good_pattern, s) is not None and re.search(bad_pattern, s) is None
    return 1 if flag else 0


def is_valid_ip_pt_2(i, s):
    good_pattern_1 = r'([a-z])(?!\1)([a-z])\1[a-z]*\[.*\2\1\2[a-z]*\]'
    good_pattern_2 = r'\[[a-z]*([a-z])(?!\1)([a-z])\1.*\][a-z]*\2\1\2'
    flag = (re.search(good_pattern_1, s) is not None) or (re.search(good_pattern_2, s) is not None)
    if flag:
        print(s)
    return 1 if flag else 0


result = 0
for i, line in enumerate(open(file)):
    result += is_valid_ip_pt_1(i, line.strip()) if part1 else is_valid_ip_pt_2(i, line.strip())
print(result)