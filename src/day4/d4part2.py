import read_input_file


def is_passport_valid(passport_line):
    '''Determines whether all the required fields of the passport are present and valid'''
    return False


def is_byr_valid(byr):
    '''(Birth Year) - four digits; at least 1920 and at most 2002.'''
    return False


def is_iyr_valid(iyr):
    '''(Issue Year) - four digits; at least 2010 and at most 2020.'''
    return False


def is_eyr_valid(eyr):
    '''(Expiration Year) - four digits; at least 2020 and at most 2030.'''
    return False


def is_hgt_valid(hgt):
    '''(Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.'''
    return False


def is_hcl_valid(hcl):
    '''(Hair Color) - a # followed by exactly six characters 0-9 or a-f.'''
    return False


def is_ecl_valid(ecl):
    '''(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.'''
    return False


def is_pid_valid(pid):
    '''(Passport ID) - a nine-digit number, including leading zeroes.'''
    return False


def how_many_passports_are_valid(passports):
    '''Determines how many passports are valid, based on whether a passport has all the required fields'''
    return 0


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day4.txt')
    print(how_many_passports_are_valid(lines))
