from functools import reduce
import read_input_file


def is_passport_valid(passport):
    '''Determines whether the passport has all the required fields, ignores optional'''
    return does_passport_have_field(passport, 'byr') and does_passport_have_field(passport, 'iyr') and does_passport_have_field(passport, 'eyr') and does_passport_have_field(passport, 'hgt') and does_passport_have_field(passport, 'hcl') and does_passport_have_field(passport, 'ecl') and does_passport_have_field(passport, 'pid')


def does_passport_have_field(passport, field_name):
    '''Determines whether a given field is present in the passport'''
    return field_name + ':' in passport


def how_many_passports_are_valid(passports):
    '''Determines how many passports are valid, based on whether a passport has all the required fields'''
    return reduce(lambda acc, passport: acc + is_passport_valid(passport), passports, 0)


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day4.txt')
    print(how_many_passports_are_valid(lines))
