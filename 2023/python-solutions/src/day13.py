# Advent of Code 2023
# Day 13

def find_horizontal_reflection(mirror: list[str], prev: int = None):
    reflections = []
    for line in mirror:
        for i in range(1, len(line)):
            start = list(reversed(line[:i]))
            end = line[i:]
            is_mirror = True
            for j in range(min(len(start), len(end))):
                if start[j] != end[j]:
                    is_mirror = False
                    break
            if is_mirror:
                reflections.append(i)
    for reflection in reflections:
        if reflection == prev:
            continue
        if (reflections.count(reflection) == len(mirror)):
            return reflection
    return 0

def find_vertical_reflection(mirror: str, prev: int = None):
    columns = [[] for _ in range(len(mirror[0]))]
    for line in mirror:
        for ind, char in enumerate(line):
            columns[ind].append(char)
    columns = [''.join(column) for column in columns]
    return find_horizontal_reflection(columns, prev)


def part_one(mirrors: list[str]):
    reflections = []
    for mirror in mirrors:
        mirror = mirror.split('\n')
        reflections.append(
            (find_horizontal_reflection(mirror), 
             find_vertical_reflection(mirror))
        )
    return sum([100*refs[1] + refs[0] for refs in reflections])

def part_two(mirrors: list[str]):
    values = []
    for mirror in mirrors:
        original_mirror = mirror.split('\n')
        original_h = find_horizontal_reflection(original_mirror)
        original_v = find_vertical_reflection(original_mirror)

        all_reflections = []
        mirror_matrix = [list(line) for line in mirror.split('\n')]
        for r, line in enumerate(mirror_matrix):
            for c, char in enumerate(line):
                mirror_matrix[r][c] = '.' if char == '#' else '#'
                unsmudged_mirror = [''.join(line) for line in mirror_matrix]
                new_h = find_horizontal_reflection(unsmudged_mirror, original_h)
                new_v = find_vertical_reflection(unsmudged_mirror, original_v)
                mirror_matrix[r][c] = char
                all_reflections.append((new_h, new_v))

        reflections = set(all_reflections)
        reflections.discard((0, 0))
        # print(f'original {(original_h, original_v)}; new {reflections}')

        value = reflections.pop()
        if value[0] != 0:
            values.append(value[0])
        else:
            values.append(value[1] * 100)
    return sum(values)

if __name__ == "__main__":
    with open("input/day13.txt") as f:
        data = f.read().split('\n\n')
    
    print('---- Part One ----')
    print(part_one(data)) # 32371

    print('---- Part Two ----')
    print(part_two(data)) # 37416
