import read_input_file


def is_passport_valid(passport):
    '''Determines whether the passport has all the required fields, ignores optional'''
    return False


def does_passport_have_field(passport, field_name):
    '''Determines whether a given field is present in the passport'''
    return False


def how_many_passports_are_valid(passports):
    '''Determines how many passports are valid, based on whether a passport has all the required fields'''
    return 0


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day4.txt')
    print(lines)
