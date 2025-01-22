import hashlib

part1 = False
file = '../input.txt'
m = hashlib.md5()

doorid = open(file).readline().strip()
print(doorid)

pw = [None for _ in range(8)]

ctr = 0
part1_i = 0
while any(x is None for x in pw):
    attempt = doorid + str(ctr)
    hashed = hashlib.md5(str.encode(attempt)).hexdigest()
    if hashed[:5] == '00000':
        if part1:
            pw[part1_i] = hashed[5]
            part1_i += 1
        else:
            pos, char = hashed[5], hashed[6]
            pos = int(pos) if pos.isdigit() else ord(pos)
            if pos < len(pw) and pw[pos] is None:
                pw[pos] = char
    ctr += 1
print(''.join(pw))