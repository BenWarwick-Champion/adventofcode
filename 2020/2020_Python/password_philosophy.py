# Advent of Code
# Day 2: Password Philosophy

def is_valid(rule, password):
    values, char = rule.split(' ')
    min, max = values.split('-')

    if (password.count(char) >= int(min) and password.count(char) <= int(max)):
        return True
    return False

def is_valid_part2(rule, password):
    values, char = rule.split(' ')
    min, max = values.split('-')
    min, max = int(min), int(max)

    if (password[min] == char and password[max] == char):
        return False
    if (password[min] == char or password[max] == char):
        return True
    return False

if __name__ == "__main__":
    # Load all the passwords
    input_file = open('Data/day2.txt')
    input_data = input_file.readlines()
    input_file.close()

    valid_passwords = 0
    for line in input_data:
        rule, password = line.split(':')
        if is_valid_part2(rule, password):
            valid_passwords += 1

    print('The number of valid passwords is:', valid_passwords)
