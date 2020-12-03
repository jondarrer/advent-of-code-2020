import d3part1


def test_can_move_1():
    the_map = ['.#.', '#.#', '##.']
    pos = {'x': 1, 'y': 1}
    actual = d3part1.can_move(the_map, pos, 1, 2)
    assert actual == True


def test_can_move_2():
    the_map = ['.#.', '#.#', '##.']
    pos = {'x': 2, 'y': 1}
    actual = d3part1.can_move(the_map, pos, 1, 2)
    assert actual == True


def test_can_move_3():
    the_map = ['.#.', '#.#', '##.']
    pos = {'x': 1, 'y': 3}
    actual = d3part1.can_move(the_map, pos, 1, 2)
    assert actual == False


def test_move_1():
    pos = {'x': 1, 'y': 1}
    actual = d3part1.move(pos, 1, 2)
    assert actual == {'x': 2, 'y': 3}


def test_what_is_in_position_1():
    the_map = ['.#.', '#.#', '##.']
    pos = {'x': 1, 'y': 1}
    actual = d3part1.what_is_in_position(the_map, pos)
    assert actual == '.'


def test_what_is_in_position_2():
    the_map = ['.#.', '#.#', '##.']
    pos = {'x': 5, 'y': 6}
    actual = d3part1.what_is_in_position(the_map, pos)
    assert actual == '#'


def test_traverse_map_at_angle_1():
    the_map = ['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.',
               '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#', '.#..#...#.#']
    start_pos = {'x': 1, 'y': 1}
    d_x = 3
    d_y = 1
    actual = d3part1.what_is_in_position(the_map, start_pos, d_x, d_y)
    assert actual == {'open': 3, 'tree': 7}
