import d3part1


def test_traverse_map_at_angle_1_1():
    the_map = ['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.',
               '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#', '.#..#...#.#']
    start_pos = {'x': 1, 'y': 1}
    d_x = 1
    d_y = 1
    actual = d3part1.traverse_map_at_angle(the_map, start_pos, d_x, d_y)
    assert actual == {'open': 8, 'tree': 2}


def test_traverse_map_at_angle_3_1():
    the_map = ['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.',
               '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#', '.#..#...#.#']
    start_pos = {'x': 1, 'y': 1}
    d_x = 3
    d_y = 1
    actual = d3part1.traverse_map_at_angle(the_map, start_pos, d_x, d_y)
    assert actual == {'open': 3, 'tree': 7}


def test_traverse_map_at_angle_5_1():
    the_map = ['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.',
               '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#', '.#..#...#.#']
    start_pos = {'x': 1, 'y': 1}
    d_x = 5
    d_y = 1
    actual = d3part1.traverse_map_at_angle(the_map, start_pos, d_x, d_y)
    assert actual == {'open': 7, 'tree': 3}


def test_traverse_map_at_angle_7_1():
    the_map = ['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.',
               '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#', '.#..#...#.#']
    start_pos = {'x': 7, 'y': 1}
    d_x = 7
    d_y = 1
    actual = d3part1.traverse_map_at_angle(the_map, start_pos, d_x, d_y)
    assert actual == {'open': 6, 'tree': 4}


def test_traverse_map_at_angle_1_2():
    the_map = ['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.',
               '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#', '.#..#...#.#']
    start_pos = {'x': 1, 'y': 1}
    d_x = 1
    d_y = 2
    actual = d3part1.traverse_map_at_angle(the_map, start_pos, d_x, d_y)
    assert actual == {'open': 3, 'tree': 2}
