import read_input_file
import d3part1


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day3.txt')
    result_1_1 = d3part1.traverse_map_at_angle(lines, {'x': 1, 'y': 1}, 1, 1)
    result_3_1 = d3part1.traverse_map_at_angle(lines, {'x': 1, 'y': 1}, 3, 1)
    result_5_1 = d3part1.traverse_map_at_angle(lines, {'x': 1, 'y': 1}, 5, 1)
    result_7_1 = d3part1.traverse_map_at_angle(lines, {'x': 1, 'y': 1}, 7, 1)
    result_1_2 = d3part1.traverse_map_at_angle(lines, {'x': 1, 'y': 1}, 1, 2)
    print(result_1_1)
    print(result_3_1)
    print(result_5_1)
    print(result_7_1)
    print(result_1_2)
    print(result_1_1['tree'] * result_3_1['tree'] *
          result_5_1['tree'] * result_7_1['tree'] * result_1_2['tree'])
