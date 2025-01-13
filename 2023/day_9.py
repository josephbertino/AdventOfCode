part_1 = False
file = '../input.txt'
sequences = [list(map(int, line.strip().split())) for line in open(file).readlines()]

results = []
for seq in sequences:
    diff = 0
    stack = [seq[0]]
    while True:
        seq = [b - a for a, b in zip(seq[0:-1], seq[1:])]
        if len(set(seq)) == 1:
            diff = seq[0]
            break
        stack.append(seq[-1] if part_1 else seq[0])

    while len(stack):
        if not part_1:
            diff *= -1
        diff += stack.pop()
    results.append(diff)

print(sum(results))