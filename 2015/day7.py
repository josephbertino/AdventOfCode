import re

part1 = False
file = '../input.txt'

groups = [re.match(r'^(.+) -> (\w+)$', line).groups() for line in open(file).readlines()]
revmap = {w.strip():op.strip() for op, w in groups}
values = dict()

BINARY_PATTERN = r'^([a-z0-9]+) ([A-Z]+) ([a-z0-9]+)$'
UNARY_PATTERN = r'^([A-Z]+) ([a-z0-9]+)$'

def get_wire_value(w):
    """
    Function that's called recursively to determine value of wire w

    :param str w:
    :return int:
    """
    global values
    global revmap

    if w.isdigit():
        return int(w)

    elif w in values:
        return values[w]

    op = revmap[w]

    if re.match(r'^\w+$', op):
        store = get_wire_value(op)
    elif re.match(BINARY_PATTERN, op): # Binary
        a, op, b = re.match(BINARY_PATTERN, op).groups()
        print(a, op, b)
        if op == 'AND':
            store = get_wire_value(a) & get_wire_value(b)
        elif op == 'OR':
            store = get_wire_value(a) | get_wire_value(b)
        elif op == 'LSHIFT':
            store = get_wire_value(a) << int(b)
        else:
            store = get_wire_value(a) >> int(b)
    else:   # Unary
        op, a = re.match(UNARY_PATTERN, op).groups()
        store = ~get_wire_value(a)

    values[w] = store
    return store

if not part1:
    values = {'b': get_wire_value('a')}

result = get_wire_value('a')
print('\nresult: ', result)