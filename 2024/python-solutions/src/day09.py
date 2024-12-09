# Advent of Code 2023
# Day 09

def parse_data(raw_data):
    i = 0
    layout = []
    for ind, char in enumerate(raw_data):
        if ind % 2 == 0:
            layout.extend([str(i)] * int(char))
            i += 1
        else:
            layout.extend(['.'] * int(char))
    return layout, i-1

def sort_data(data):
    mutated_data = list(reversed(data))
    sorted_data = []
    total = len(data) - data.count('.')
    for char in data:
        if len(sorted_data) == total:
            break
        if char == '.':
            for i, c in enumerate(mutated_data):
                if c != '.':
                    mutated_data[i] = '.'
                    sorted_data.append(c)
                    break
        else:
            sorted_data.append(char)
    return sorted_data
            
def checksum(data):
    total = 0
    for block in data:
        start, end = data[block]
        for i in range(start, end+1):
            total += i * int(block)
    return total

def part_one(raw_data):
    data, _ = parse_data(raw_data)
    # print(data)
    sorted_data = sort_data(data)

    return sum([i*int(c) for i, c in enumerate(sorted_data)])

def part_two(raw_data):
    data, _ = parse_data(raw_data)

    blocks = dict()
    empty_slots = dict()

    i = 0
    curr = data[i]
    start_index = 0
    while i < len(data):
        if data[i] != curr:
            start_index = i
            curr = data[i]
        if data[i] == '.':
            empty_slots[start_index] = empty_slots.get(start_index, 0) + 1
        else:
            blocks[data[i]] = (start_index, i)

        i += 1

    for block in reversed(blocks):
        start, end = blocks[block]
        print('Block:', block, 'Start:', start, 'End:', end)
        length = end - start + 1

        for slot in sorted(int(key) for key in empty_slots.keys()):
            # print('Slot:', slot)
            if empty_slots[slot] >= length and slot < start:
                # print('Filling slot:', slot)
                # print('Remaining:', empty_slots[slot] - length)
                remaining_spaces = empty_slots[slot] - length
                if remaining_spaces > 0:
                    empty_slots[slot+length] = remaining_spaces
                del empty_slots[slot]

                empty_slots[start] = length
                blocks[block] = (slot, slot+length-1)
                # print('Empty slots:', empty_slots)
                # print('Blocks:', blocks)
                break

    return checksum(blocks)

if __name__ == "__main__":
    with open("input/day09.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 6330095022244

    print('---- Part Two ----')
    print(part_two(raw_data)) # 6359491814941
