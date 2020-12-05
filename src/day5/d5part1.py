import read_input_file


def convert_boarding_pass_to_seat(boarding_pass):
    '''Converts a boarding pass, e.g. FBFBBFFRLR, to seat, e.g. row 44 column 5'''
    row = convert_binary_to_decimal(boarding_pass[0:7], 'B')
    column = convert_binary_to_decimal(boarding_pass[7:10], 'R')
    return {'row': row, 'column': column}


def convert_seat_to_seat_id(seat):
    '''The seat as a seat id, e.g. row 44 column 5 is seat id 357 (row + (column * 8))'''
    return seat['row'] * 8 + seat['column']


def convert_binary_to_decimal(binary, one_char):
    '''Converts a binary number to decimal, with a specified character for 1, so FBF with B as 1 gives 3'''
    decimal = 0
    # https://www.w3schools.com/python/python_howto_reverse_string.asp
    for index, bit in enumerate(binary[::-1]):
        if (bit == one_char):
            decimal += (2 ** index + 1) - 1

    return decimal


def highest_seat_id_from_boarding_passes(boarding_passes):
    '''The highest seat id from a list of boarding passes'''
    boarding_pass_with_highest_seat_id = max(boarding_passes, key=lambda boarding_pass: convert_seat_to_seat_id(
        convert_boarding_pass_to_seat(boarding_pass)))
    return convert_seat_to_seat_id(convert_boarding_pass_to_seat(boarding_pass_with_highest_seat_id))


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day5.txt')
    print(highest_seat_id_from_boarding_passes(lines))
