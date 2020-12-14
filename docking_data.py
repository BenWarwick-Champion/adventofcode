# Advent of Code 2020
# Day 14: Docking Data

if __name__ == "__main__":
    with open("Data/day14.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    max_address = 0
    for line in data:
        if 'mem' in line:
            addr = line.split(' = ')[0]
            address = int(addr[4:-1])
            if address > max_address: max_address = address

    mask = []
    mem = [0] * (max_address + 1)
    for line in data:
        if 'mask' in line:
            mask = list(line.split(' = ')[1])
        else:
            addr, val = line.split(' = ')
            value = list(bin(int(val))[2:].zfill(36))
            for ind, char in enumerate(mask):
                if char != 'X':
                    value[ind] = char
            insert = int("".join(value), 2)
            mem[int(addr[4:-1])] = insert

    part1 = sum(mem)
    print("Part 1 solution is:", part1)
        