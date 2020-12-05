import d5part1
import read_input_file


def first_missing_seat_id_from_boarding_passes(boarding_passes):
    '''The missing seat id from a list of boarding passes'''
    seat_ids = list(map(lambda boarding_pass: d5part1.convert_seat_to_seat_id(
        d5part1.convert_boarding_pass_to_seat(boarding_pass)), boarding_passes))
    seat_ids.sort()
    index = 0
    while seat_ids[index] - seat_ids[index + 1] == -1 and index < len(seat_ids):
        index += 1
    return seat_ids[index] + 1


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day5.txt')
    print(first_missing_seat_id_from_boarding_passes(lines))
