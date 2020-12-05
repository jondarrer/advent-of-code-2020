import d5part1


def test_convert_boarding_pass_to_seat_1():
    boarding_pass = 'FBFBBFFRLR'
    actual = d5part1.convert_boarding_pass_to_seat(boarding_pass)
    assert actual == {'row': 44, 'column': 5}


def test_convert_boarding_pass_to_seat_2():
    boarding_pass = 'BFFFBBFRRR'
    actual = d5part1.convert_boarding_pass_to_seat(boarding_pass)
    assert actual == {'row': 70, 'column': 7}


def test_convert_boarding_pass_to_seat_3():
    boarding_pass = 'FFFBBBFRRR'
    actual = d5part1.convert_boarding_pass_to_seat(boarding_pass)
    assert actual == {'row': 14, 'column': 7}


def test_convert_boarding_pass_to_seat_4():
    boarding_pass = 'BBFFBBFRLL'
    actual = d5part1.convert_boarding_pass_to_seat(boarding_pass)
    assert actual == {'row': 102, 'column': 4}


def test_convert_binary_to_decimal_b_1():
    binary = 'FBFBBFF'
    actual = d5part1.convert_binary_to_decimal(binary, 'B')
    assert actual == 44


def test_convert_binary_to_decimal_b_2():
    binary = 'BFFFBBF'
    actual = d5part1.convert_binary_to_decimal(binary, 'B')
    assert actual == 70


def test_convert_binary_to_decimal_b_3():
    binary = 'FFFBBBF'
    actual = d5part1.convert_binary_to_decimal(binary, 'B')
    assert actual == 14


def test_convert_binary_to_decimal_b_4():
    binary = 'BBFFBBF'
    actual = d5part1.convert_binary_to_decimal(binary, 'B')
    assert actual == 102


def test_convert_binary_to_decimal_r_1():
    binary = 'RLR'
    actual = d5part1.convert_binary_to_decimal(binary, 'R')
    assert actual == 5


def test_convert_binary_to_decimal_r_2():
    binary = 'RRR'
    actual = d5part1.convert_binary_to_decimal(binary, 'R')
    assert actual == 7


def test_convert_binary_to_decimal_r_3():
    binary = 'RLL'
    actual = d5part1.convert_binary_to_decimal(binary, 'R')
    assert actual == 4


def test_convert_seat_to_seat_id_1():
    seat = {'row': 44, 'column': 5}
    actual = d5part1.convert_seat_to_seat_id(seat)
    assert actual == 357


def test_convert_seat_to_seat_id_2():
    seat = {'row': 70, 'column': 7}
    actual = d5part1.convert_seat_to_seat_id(seat)
    assert actual == 567


def test_convert_seat_to_seat_id_3():
    seat = {'row': 14, 'column': 7}
    actual = d5part1.convert_seat_to_seat_id(seat)
    assert actual == 119


def test_convert_seat_to_seat_id_4():
    seat = {'row': 102, 'column': 4}
    actual = d5part1.convert_seat_to_seat_id(seat)
    assert actual == 820


def test_highest_seat_id_from_boarding_passes():
    boarding_pass_1 = 'FBFBBFFRLR'
    boarding_pass_2 = 'BFFFBBFRRR'
    boarding_pass_3 = 'FFFBBBFRRR'
    boarding_pass_4 = 'BBFFBBFRLL'
    actual = d5part1.highest_seat_id_from_boarding_passes(
        [boarding_pass_1, boarding_pass_2, boarding_pass_3, boarding_pass_4])
    assert actual == 820
