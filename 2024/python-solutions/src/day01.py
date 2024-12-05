from collections import Counter

def part_one(raw_data):
    l1, l2 = [], []
    for line in raw_data:
        a, b = line.split('   ')
        l1.append(int(a))
        l2.append(int(b))
      
    l1.sort()
    l2.sort()
    sorted_pairs = list(zip(l1, l2))
    total = 0
    for pair in sorted_pairs:
        a, b = pair

        total += abs(a - b)
    return total

def part_two(raw_data):
    l1, l2 = [], []
    for line in raw_data:
        a, b = line.split('   ')
        l1.append(int(a))
        l2.append(int(b))

    lookup = Counter(l2)

    total = 0
    for num in l1:
        if lookup[num] == 0:
            continue
        else:
            total += num * lookup[num]

    return total

if __name__ == "__main__":
    with open("input/day01.txt") as f:
        raw_data = f.readlines()
    
    print('---- Part One ----')
    print(part_one(raw_data))

    print('---- Part Two ----')
    print(part_two(raw_data))