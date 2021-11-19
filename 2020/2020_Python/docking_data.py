# Advent of Code 2020
# Day 14: Docking Data

def find_max_addr(data):
    max_address = 0
    for line in data:
        if 'mem' in line:
            addr = line.split(' = ')[0]
            address = int(addr[4:-1])
            if address > max_address: max_address = address
    return max_address + 1


def part1(data, max_addr):
    mask = []
    mem = [0] * max_addr
    for line in data:
        if 'mask' in line:
            mask = list(line.split(' = ')[1])
        else:
            addr, val = line.split(' = ')
            value = list(bin(int(val))[2:].zfill(36))
            for ind, char in enumerate(mask):
                if char != 'X':
                    value[ind] = char
            mem[int(addr[4:-1])] = int("".join(value), 2)
    return mem


def apply_mask(arg, mask):
    arg |= int(mask.replace('X', '0'), 2)
    arg &= int(mask.replace('X', '1'), 2)
    return arg


def unpack_mask(mask):
    if not mask:
        yield ''
        return
    for m in unpack_mask(mask[1:]):
        if mask[0] == '0':
            yield 'X' + m
        elif mask[0] == '1':
            yield '1' + m
        elif mask[0] == 'X':
            yield '0' + m
            yield '1' + m


def part2(data):
    mem = {}
    mask = ''
    for line in data:
        addr, val = line.split(' = ')
        if 'mask' in addr:
            mask = val
        else:
            address = int(addr[4:-1])
            for m in unpack_mask(mask):
                mem[apply_mask(address, m)] = int(val)
    return mem


if __name__ == "__main__":
    with open("Data/day14.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    max_address = find_max_addr(data)
    part1 = sum(part1(data, max_address))
    print("Part 1 solution is:", part1)

    part2 = sum(part2(data).values())
    print("Part 2 solution is:", part2)
        