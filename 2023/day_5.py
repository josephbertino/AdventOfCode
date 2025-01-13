import re
import math

file = '../input.txt'
part_1 = False

# Parse Input
contents = open(file).read().split('\n\n')
seeds = list(map(int, re.findall(r'\d+', contents[0])))

if part_1:
    seed_ranges = [(val, val) for val in seeds]
else:
    seed_ranges = [(start, start+span-1) for start, span in zip(seeds[::2], seeds[1::2])]

map_levels = []
for s in contents[1:]:
    level = [[int(sss) for sss in ss.split()] for ss in s.split('\n')[1:]]
    map_levels.append(sorted(level, key=lambda x: x[1]))

# Work through seed ranges
result = math.inf
for seed_range in seed_ranges:
    seed_range_start = seed_range[0]
    seed_range_end = seed_range[1]
    curr_intervals = [seed_range]

    for level in map_levels:
        new_intervals = []
        for int_start, int_end in curr_intervals:
            LMV = int_start - 1     # Last Mapped Value
            for dest_start, source_start, span_max in level:
                source_end = source_start + span_max - 1
                dest_end = dest_start + span_max - 1
                if source_start <= int_end and source_end >= int_start:
                    if LMV + 1 < source_start:
                        new_intervals.append((LMV + 1, source_start - 1))
                    LMV = source_end

                    from_source_start = max(0, int_start - source_start)
                    from_source_end = max(0, source_end - int_end)

                    new_intervals.append((dest_start + from_source_start, dest_end - from_source_end))
            if LMV < int_end:
                new_intervals.append((LMV + 1, int_end))
        curr_intervals = new_intervals

    lowest = sorted(curr_intervals, key=lambda x: x[0])[0][0]
    if lowest < result:
        result = lowest

print(result)
