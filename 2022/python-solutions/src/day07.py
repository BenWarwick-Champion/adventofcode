# Advent of Code 2022
# Day 07

from collections import defaultdict


def parse_files(lines):
    dirs = defaultdict(int)
    for line in lines:
        match line.strip().split():
            case '$', 'cd', '/':
                pwd = ['/']
            case '$', 'cd', '..':
                pwd.pop()
            case '$', 'cd', dirName:
                pwd.append(dirName + '/')
            case '$', 'ls':
                pass
            case 'dir', _dirName:
                pass
            case size, _fileName:
                path = ''
                for path_section in pwd:
                    path += path_section
                    dirs[path] += int(size)
    return dirs


def dir_to_delete(dirs):
    total = 70_000_000
    needed = 30_000_000
    used = dirs['/']
    threshold = used - (total - needed)

    smallest = total
    for dirName in dirs:
        if dirs[dirName] > threshold and dirs[dirName] < smallest:
            smallest = dirs[dirName]
    return smallest


if __name__ == "__main__":
    with open("input/day07.txt") as f:
        data = f.readlines()
    dirs = parse_files(data)

    print('---- Part One ----')
    print(sum([dirs[dirName]
          for dirName in dirs if dirs[dirName] < 100_000]))  # 1432936

    print('---- Part Two ----')
    print(dir_to_delete(dirs))  # 272298
