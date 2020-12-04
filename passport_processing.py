# Advent of Code 2020
# Day 4: Password Processing

def is_valid(passport):
    check_keys = ['byr', 'iyr', 'eyr', 'hgt',
                  'hcl', 'ecl', 'pid']
    if all(key in passport for key in check_keys):
        return True
    return False


def is_valid_all(passport_dict):
    if (
        valid_byr(passport_dict)
        and valid_iyr(passport_dict)
        and valid_eyr(passport_dict)
        and valid_hgt(passport_dict)
        and valid_hcl(passport_dict)
        and valid_ecl(passport_dict)
        and valid_pid(passport_dict)
    ):
        return True
    return False


def valid_byr(passport_dict):
    if passport_dict.get('byr') is None:
        return False
    byr = int(passport_dict.get('byr'))
    if (1920 <= byr and byr <= 2002):
        return True
    return False


def valid_iyr(passport_dict):
    if passport_dict.get('iyr') is None:
        return False
    iyr = int(passport_dict.get('iyr'))
    if (2010 <= iyr and iyr <= 2020):
        return True
    return False


def valid_eyr(passport_dict):
    if passport_dict.get('eyr') is None:
        return False
    eyr = int(passport_dict.get('eyr'))
    if (2020 <= eyr and eyr <= 2030):
        return True
    return False


def valid_hgt(passport_dict):
    hgt = passport_dict.get('hgt')
    if hgt is None:
        return False
    num, unit = hgt[:-2], hgt[-2:]
    if (unit == 'cm' and len(num) == 3 and num.isnumeric()):
        if (150 <= int(num) <= 193):
            return True
        return False
    elif (unit == 'in' and len(num) == 2 and num.isnumeric()):
        if (59 <= int(num) <= 76):
            return True
        return False
    else:
        return False


def valid_hcl(passport_dict):
    hcl = passport_dict.get('hcl')
    if hcl is None:
        return False
    hash, code = hcl[0], hcl[1:]
    if hash != '#':
        return False
    if (len(code) == 6 and code.isalnum()):
        return True
    return False


def valid_ecl(passport_dict):
    ecl = passport_dict.get('ecl')
    if ecl is None:
        return False
    colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if (ecl in colours):
        return True
    return False


def valid_pid(passport_dict):
    pid = passport_dict.get('pid')
    if pid is None:
        return False
    if (len(pid) == 9 and pid.isnumeric()):
        return True
    return False


if __name__ == "__main__":
    with open("Data/day4.txt", "r") as f:
        input_data = f.readlines()

    lastline = ''
    passports = []
    for line in input_data:
        if line == '\n':
            passports.append(lastline)
            lastline = ''
        else:
            lastline = (lastline + line).replace('\n', ' ')
    passports.append(lastline)

    print("Number of passports:", len(passports))

    count = 0
    for passport in passports:
        if is_valid(passport):
            count += 1

    print(f'There are {count} part 1 valid passports')

    pass_dict_list = []
    for passport in passports:
        pass_dict = dict()
        split_pass = passport.split()
        for item in split_pass:
            key, value = item[:3], item[4:]
            pass_dict.setdefault(key, value)
        pass_dict_list.append(pass_dict)

    count2 = 0
    for p_dict in pass_dict_list:
        if is_valid_all(p_dict):
            count2 += 1

    print(f'There are {count2} part 2 valid passports')
