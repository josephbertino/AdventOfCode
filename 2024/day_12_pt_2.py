from collections import defaultdict

file = 'input.txt'
garden = {i+j*1j: c for i, line in enumerate(open(file).readlines()) for j, c in enumerate(line.strip())}
H = int(max(map(lambda x: x.real, garden.keys())) + 1)
W = int(max(map(lambda x: x.imag, garden.keys())) + 1)
print(H, W, garden)

coord_to_region = defaultdict(int)
region_area = defaultdict(int)

def explore_region(coord, plot_char, region_id):
    if (coord not in garden) or (coord in coord_to_region) or plot_char != garden[coord]:
        return
    coord_to_region[coord] = region_id
    region_area[region_id] += 1
    for d in [1, 1j, -1, -1j]:
        explore_region(coord+d, plot_char, region_id)

# Identify Regions and Get Areas
region_id = 1
for r in range(H):
    for c in range(W):
        coord = r + c*1j
        if coord not in coord_to_region:
            # region_id = garden[coord]
            plot_char = garden[coord]
            explore_region(coord, plot_char, region_id)
            region_id += 1

region_sides = defaultdict(int)
# Log Region Sides
prev_TOP = prev_BOT = 0
for r in range(H+1):
    for c in range(W):
        curr_TOP = coord_to_region.get((r-1)+c*1j, 0)
        curr_BOT = coord_to_region.get(r+c*1j, 0)
        if curr_BOT != curr_TOP:
            region_sides[curr_TOP] += 1 if (curr_TOP != prev_TOP or prev_TOP == prev_BOT) else 0
            region_sides[curr_BOT] += 1 if (curr_BOT != prev_BOT or prev_TOP == prev_BOT) else 0
        prev_TOP = curr_TOP
        prev_BOT = curr_BOT

prev_LEFT = prev_RIGHT = 0
for c in range(W+1):
    for r in range(H):
        curr_LEFT = coord_to_region.get(r + (c - 1) * 1j, 0)
        curr_RIGHT = coord_to_region.get(r + c * 1j, 0)
        if curr_LEFT != curr_RIGHT:
            region_sides[curr_LEFT] += 1 if (curr_LEFT != prev_LEFT or prev_LEFT == prev_RIGHT) else 0
            region_sides[curr_RIGHT] += 1 if (curr_RIGHT != prev_RIGHT or prev_LEFT == prev_RIGHT) else 0
        prev_LEFT = curr_LEFT
        prev_RIGHT = curr_RIGHT

print(coord_to_region)
print(region_area)
print(region_sides)

result = sum(area * region_sides[region_id] for region_id, area in region_area.items())
print(result)