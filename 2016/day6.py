# Read lines from file
file = '../input.txt'
lines = [line.strip() for line in open(file, 'r')]

# Get line length
line_length = len(lines[0].strip())

# Initialize frequency tracking
position_frequencies = [{} for _ in range(line_length)]

# Count character frequencies per position
for line in lines:
    for pos, char in enumerate(line.strip()):
        position_frequencies[pos][char] = position_frequencies[pos].get(char, 0) + 1

# Find most frequent character for each position
most_frequent_chars = [
    min(freq_dict, key=freq_dict.get)
    for freq_dict in position_frequencies
]

# Print result
print("Most frequent characters per position:", ''.join(most_frequent_chars))