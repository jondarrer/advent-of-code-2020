import re
from functools import reduce
import read_input_file


def is_passport_valid(passport_line):
    '''Determines whether all the required fields of the passport are present and valid'''
    passport = {'byr': '', 'iyr': '', 'eyr': '',
                'hgt': '', 'hcl': '', 'ecl': '', 'pid': ''}
    for line_part in passport_line.split(' '):
        part_bits = line_part.split(':')
        passport[part_bits[0]] = part_bits[1]

    return is_byr_valid(passport['byr']) and is_iyr_valid(passport['iyr']) and is_eyr_valid(passport['eyr']) and is_hgt_valid(passport['hgt']) and is_hcl_valid(passport['hcl']) and is_ecl_valid(passport['ecl']) and is_pid_valid(passport['pid'])


def is_byr_valid(byr):
    '''(Birth Year) - four digits; at least 1920 and at most 2002.'''
    return string_number_between(byr, 1920, 2002, 4)


def is_iyr_valid(iyr):
    '''(Issue Year) - four digits; at least 2010 and at most 2020.'''
    return string_number_between(iyr, 2010, 2020, 4)


def is_eyr_valid(eyr):
    '''(Expiration Year) - four digits; at least 2020 and at most 2030.'''
    return string_number_between(eyr, 2020, 2030, 4)


hgt_regex = re.compile(r'^(?P<size>\d{1,3})(?P<unit>cm|in)$')


def is_hgt_valid(hgt):
    '''(Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.'''
    hgt_obj = hgt_regex.match(hgt)
    if (hgt_obj != None):
        if (hgt_obj['unit'] == 'cm'):
            return string_number_between(hgt_obj['size'], 150, 193)
        else:
            return string_number_between(hgt_obj['size'], 59, 76)
    return False


hcl_regex = re.compile(r'^#[0-9a-fA-F]{6}$')


def is_hcl_valid(hcl):
    '''(Hair Color) - a # followed by exactly six characters 0-9 or a-f.'''
    return hcl_regex.match(hcl) != None


def is_ecl_valid(ecl):
    '''(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.'''
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


pid_regex = re.compile(r'^[0-9]{9}$')


def is_pid_valid(pid):
    '''(Passport ID) - a nine-digit number, including leading zeroes.'''
    return pid_regex.match(pid) != None


def how_many_passports_are_valid(passports):
    '''Determines how many passports are valid, based on whether a passport has all the required fields and those fields are valid'''
    return reduce(lambda acc, passport: acc + is_passport_valid(passport), passports, 0)


def string_number_between(str_num, min_num, max_max, length=-1):
    if (length != -1 and len(str_num) != length):
        return False
    if (is_integer(str_num)):
        int_num = int(str_num)
        return min_num <= int_num <= max_max
    return False


# https://note.nkmk.me/en/python-check-int-float/
def is_integer(n):
    '''True is the string is an integer, False otherwise'''
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day4.txt')
    print(how_many_passports_are_valid(lines))
