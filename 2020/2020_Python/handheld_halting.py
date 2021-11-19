# Advent of Code 2020
# Day 8: Handheld Halting

def acc_op(accumulator, num):
    accumulator += int(num)
    return accumulator


def jmp_op(readhead, num):
    readhead += int(num)
    return readhead


def process_code(raw_code):
    return [line.strip('\n') for line in raw_code]


def run(code):
    acc, read_head = 0, 0
    seen = []
    while(read_head < len(code)):
        instr = code[read_head].split()
        if read_head in seen: break
        seen.append(read_head)
        if instr[0] == 'acc': acc = acc_op(acc, instr[1])
        if instr[0] == 'jmp':
            read_head = jmp_op(read_head, instr[1])
            continue
        read_head += 1
    return acc, read_head, seen


def run_mod(code, seen):
    '''Version of run() to allow the modification of instructions'''
    for line in seen:
        acc, read_head = 0, 0
        new_seen = []
        while(read_head < len(code)):
            instr = code[read_head].split()
            if read_head in new_seen: break
            if read_head == line:
                if instr[0] == 'jmp': instr[0] = 'nop'
                elif instr[0] == 'nop': instr[0] = 'jmp'
            new_seen.append(read_head)
            if instr[0] == 'acc': acc = acc_op(acc, instr[1])
            if instr[0] == 'jmp':
                read_head = jmp_op(read_head, instr[1])
                continue
            read_head += 1
        if read_head == len(code):
            return acc, read_head, new_seen
    return "Error no succesful instruction modification found."


if __name__ == "__main__":
    with open("Data/day8.txt", "r") as f:
        input_data = f.readlines()
    code = process_code(input_data)

    ########### Part 1 ##########
    acc, read_head, seen = run(code)
    print("Accumulator value is:", acc)  # 1501
    print("Read head is at line:", read_head)  # 47
    print("Instructions executed:", len(seen))  # 205

    ########### Part 2 ###########
    acc, read_head, seen = run_mod(code, seen)
    print("Accumulator value is:", acc) # 509
    print("Read head is at line:", read_head) # 636
    print("Instructions executed:", len(seen)) # 57
