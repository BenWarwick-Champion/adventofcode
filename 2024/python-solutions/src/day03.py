# Advent of Code 2023
# Day 03

def force_int(val: str):
    try:
        return int(val)
    except ValueError:
        return 0

def part_one(raw_data):
    total = 0
    for i in range(len(raw_data)):
        if raw_data[i] != 'm':
            continue

        mul = raw_data[i:i+4]

        if mul != 'mul(':
            print('invalid mul:', mul)
            i += 4
            continue

        print('Parsing:', mul, 'pos:', i)

        start = i + 4
        end = i + 5
        for j in range(i, len(raw_data)):
            if raw_data[j] == '':
                print('eof')
                break
            if raw_data[j] == ')':
                end = j
                break
        
        instr = raw_data[start:end]
        print('found instr:', instr)

        if ',' not in instr:
            print('no comma')
            i += 4
            continue

        if instr.count(',') != 1:
            print('too many commas')
            i += 4
            continue

        nums = instr.split(',')
        a = force_int(nums[0])
        b = force_int(nums[1])
        print('a:', a, 'b:', b)

        result = a * b
        total += result
    return total

def part_two(raw_data):
    total = 0
    mul_enabled = True
    for i in range(len(raw_data)):
        if raw_data[i] == 'd':
            do = raw_data[i:i+4]
            dont = raw_data[i:i+7]

            if do == 'do()':
                mul_enabled = True
                continue
            if dont == "don't()":
                mul_enabled = False
                continue

            continue

        if raw_data[i] != 'm':
            continue

        mul = raw_data[i:i+4]

        if mul != 'mul(':
            print('invalid mul:', mul)
            i += 4
            continue

        print('Parsing:', mul, 'pos:', i)

        start = i + 4
        end = i + 5
        for j in range(i, len(raw_data)):
            if raw_data[j] == '':
                print('eof')
                break
            if raw_data[j] == ')':
                end = j
                break
        
        instr = raw_data[start:end]
        print('found instr:', instr)

        if ',' not in instr:
            print('no comma')
            i += 4
            continue

        if instr.count(',') != 1:
            print('too many commas')
            i += 4
            continue

        nums = instr.split(',')
        a = force_int(nums[0])
        b = force_int(nums[1])
        print('a:', a, 'b:', b)

        result = a * b
        if mul_enabled:
            total += result
    return total

if __name__ == "__main__":
    with open("input/day03.txt") as f:
        raw_data = f.read()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 173785482

    print('---- Part Two ----')
    print(part_two(raw_data)) # 83158140
