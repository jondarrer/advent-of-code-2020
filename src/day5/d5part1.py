import read_input_file


def convert_boarding_pass_to_seat(boarding_pass):
    '''Converts a boarding pass, e.g. FBFBBFFRLR, to seat, e.g. row 55 column 5'''
    return {'row': 0, 'column': 0}


def convert_seat_to_seat_id(seat):
    ''''''
    return 0


def convert_binary_to_decimal(binary, one_char):
    '''Converts a binary number to decimal, with a specified character for 1, so FBF with B as 1 gives 3'''
    return 0


def highest_seat_id_from_boarding_passes(boarding_passes):
    '''The highest seat id from a list of boarding passes'''
    return 0


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day5.txt')
    print(lines)
