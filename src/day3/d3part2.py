import read_input_file
import d3part1


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day3.txt')
    print(len(lines))
    result = d3part1.traverse_map_at_angle(lines, {'x': 1, 'y': 1}, 3, 1)
    print(result)
