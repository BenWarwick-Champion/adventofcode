# Advent of Code 2020
# Day 25: Combo Breaker
# Merry Christmas!

def find_loopsize(sub_num, public_key):
    result = 1
    count = 0
    while result != public_key:
        result *= sub_num
        result = result % 20201227
        count += 1
    return count

def calc_encryption_key(public_key, loop_size):
    result = 1
    for _ in range(loop_size):
        result *= public_key
        result = result % 20201227
    return result

if __name__ == "__main__":
    with open("Data/day25.txt", "r") as f:
        data = [int(line.strip()) for line in f.readlines()]
    card_public, door_public = data[0], data[1]

    subject_number = 7

    card_loop = find_loopsize(subject_number, card_public)
    door_loop = find_loopsize(subject_number, door_public)

    enc_key = calc_encryption_key(door_public, card_loop)

    print("Part 1 solution:", enc_key)
    