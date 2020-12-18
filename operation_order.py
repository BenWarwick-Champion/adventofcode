# Advent of Code 2020
# Day 18: Operation Order

def find_nth(string, match, n):
    ind = string.find(match)
    if n > 1:
        for _ in range(n-1):
            ind = string.find(match, ind + 1)
    return ind


# '(7 * 2 + 3 + 5)' or '7 * 2 + 3 + 5'
def evaluate(string):
    if '(' in string:
        eq = string[1:-1].split()
    else:
        eq = string.split()

    while len(eq) > 3:
        equation = ''.join(eq[:3])
        res = eval(equation)
        for _ in range(3):
            eq.pop(0)
        eq.insert(0, str(res))
    
    ans = eval(''.join(eq))
    return ans


def eval_backwards(string):
    if '(' in string:
        eq = string[1:-1].split()
    else:
        eq = string.split()

    while eq.count('+') > 0:
        ind = eq.index('+')
        res = int(eq[ind-1]) + int(eq[ind+1])
        for _ in range(3):
            eq.pop(ind-1)
        eq.insert(ind-1, str(res))
    
    ans = eval(''.join(eq))
    return ans


if __name__ == "__main__":
    with open("Data/day18.txt", "r") as f:
        hw = [line.strip() for line in f.readlines()]

    hw_sum = 0
    for line in hw:
        ob = line.count('(')
        lastline = line
        while ob > 0:
            start = find_nth(lastline, '(', ob)
            end = lastline.find(')', start) + 1
            result = evaluate(lastline[start:end])
            newline = lastline.replace(lastline[start:end], str(result))
            lastline = newline
            ob -= 1
        hw_sum += evaluate(lastline)

    print("Part 1 solution:", hw_sum) # 21022630974613

    hw_sum = 0
    for line in hw:
        ob = line.count('(')
        lastline = line
        while ob > 0:
            start = find_nth(lastline, '(', ob)
            end = lastline.find(')', start) + 1
            result = eval_backwards(lastline[start:end])
            newline = lastline.replace(lastline[start:end], str(result))
            lastline = newline
            ob -= 1
        hw_sum += eval_backwards(lastline)

    print("Part 2 solution:", hw_sum) # 169899524778212
