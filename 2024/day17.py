part1 = False
A, B, C = 0, 1, 2
file = '../input.txt'

f = open(file)
lines = f.readlines()

register = list(map(int, [line.split(': ')[1].strip() for line in lines[:3]]))
pgm = list(map(int, lines[4].split(': ')[1].strip().split(',')))
output = []

def get_register_val(val):
    return register[val]

def get_combo_val(val: int):
    if 0 <= val <= 3:
        return val
    else:
        return get_register_val(val-4)

def adv(ip, val):
    register[A] = register[A] // 2**get_combo_val(val)
    return ip + 1

def bxl(ip, val):
    register[B] = register[B] ^ val
    return ip + 1

def bst(ip, val):
    register[B] = get_combo_val(val) % 8
    return ip + 1

def jnz(ip, val):
    if register[A]:
        return val // 2
    return ip + 1

def bxc(ip, val):
    register[B] ^= register[C]
    return ip + 1

def out(ip, val):
    output.append(str(get_combo_val(val) % 8))
    return ip + 1

def cdv(ip, val):
    register[C] = register[A] // (2 ** get_combo_val(val))
    return ip + 1

opmap = {0:adv, 1:bxl, 2:bst, 3:jnz, 4:bxc, 5:out, 7:cdv}

program = [(pos, code) for pos, code in zip(pgm[::2], pgm[1::2])]
n = len(program)

def perform_op(ip):
    op, val = program[ip]
    return opmap[op](ip, val)

if part1:
    ip = 0
    while ip < n:
        ip = perform_op(ip)
    print(','.join(output))
else:
    revpgm = pgm[::-1]

    def get_out(a):
        return (1 ^ (a % 8) ^ (a // (2 ** ((a % 8) ^ 2)))) % 8

    def find_a(i, a):
        if i == len(revpgm):
            return a // 8
        v = revpgm[i]
        for x in range(8):
            if get_out(a + x) == v:
                final = find_a(i + 1, (a + x) * 8)
                if final is not None:
                    return final
        return None

    print(find_a(0, 0))


"""
2,4,1,2,7,5,1,3,4,3,5,5,0,3,3,0 

Program: 
(2, 4) <---- B = A % 8
(1, 2) <---- B ^= 2
(7, 5) <---- C = A // (2 ** B)
(1, 3) <---- B ^= 3
(4, 3) <---- B ^= C
(5, 5) <----  print(B % 8)
(0, 3) <----  A = A // 8
(3, 0) <----  jump to 0 if A 

Condensed: 
B = 1 ^ (A % 8) ^ (A // (2 ** ((A % 8) ^ 2)))
print(B % 8)
A = A // 8
Jump to 0 if A

"""
