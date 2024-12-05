# Advent of Code 2023
# Day 02

def safe_report(report, removeIndex=None):
    levels = [int(i) for i in report.split()]
    if removeIndex is not None:
        del levels[removeIndex]
    safe = True
    increasing = bool(levels[0] < levels[1])
    for i, level in enumerate(levels):
        if i == 0:
            continue
        diff = abs(levels[i-1] - level)
        if levels[i-1] == level:
            safe = False
            break
        if (levels[i-1] < level) != increasing:
            safe = False
            break
        if diff > 3:
            safe = False
    return safe


def part_one(raw_data):
    safe_reports = 0
    for index, report in enumerate(raw_data):
        safe = safe_report(report)
        print('Report:', index, 'Safe:', safe)
        if safe:
            safe_reports += 1
    return safe_reports

def part_two(raw_data):
    safe_reports = 0
    for index, report in enumerate(raw_data):
        safe = safe_report(report)
        if not safe:
            for index, _ in enumerate(report.split()):
                safe = safe_report(report, index)
                if safe:
                    break
        if safe:
            safe_reports += 1
    return safe_reports

if __name__ == "__main__":
    with open("input/day02_lizzie.txt") as f:
        raw_data = f.readlines()
    
    print('---- Part One ----')
    print(part_one(raw_data)) # 230

    print('---- Part Two ----')
    print(part_two(raw_data)) # 301
