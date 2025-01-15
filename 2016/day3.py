part1 = False
file = '../input.txt'

tris = [list(map(int, line.strip().split())) for line in open(file).readlines()]

if not part1:
    N_groups = len(tris) // 3
    tris = [grp for i in range(N_groups) for grp in zip(tris[i*3], tris[(i*3)+1], tris[(i*3)+2])]

result = 0
for a, b, c in tris:
    if a + b > c and a + c > b and b + c > a:
        result += 1

print(result)
