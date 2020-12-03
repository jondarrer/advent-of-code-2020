import read_input_file


def can_move(the_map, pos, d_x, d_y):
    '''Determines whether or not the desired move can be made or not'''
    if (len(the_map) < pos['y'] + d_y):
        return False
    return True


def move(pos, d_x, d_y):
    '''Moves to the desired position, '''
    return {'x': pos['x'] + d_x, 'y': pos['y'] + d_y}


def what_is_in_position(the_map, pos):
    '''Determines what is at the current postion on the map, wrapping along both axis when necessary'''
    map_y = (pos['y'] - 1) % len(the_map)
    line = the_map[map_y]
    map_x = (pos['x'] - 1) % len(line)
    return line[map_x]


def traverse_map_at_angle(the_map, start_pos, d_x, d_y):
    '''Traverses the map, repeating along the x axis only, outputting the number of open and tree spaces encountered'''

    result = {'open': 0, 'tree': 0}
    pos = start_pos

    while can_move(the_map, pos, d_x, d_y):
        pos = move(pos, d_x, d_y)
        if (what_is_in_position(the_map, pos) == '.'):
            result['open'] = result['open'] + 1
        else:
            result['tree'] = result['tree'] + 1

    return result


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day3.txt')
    print(len(lines))
    result = traverse_map_at_angle(lines, {'x': 1, 'y': 1}, 3, 1)
    print(result)
