import read_input_file


def can_move(the_map, pos, d_x, d_y):
    '''Determines whether or not the desired move can be made or not'''
    return False


def move(pos, d_x, d_y):
    '''Moves to the desired position, '''
    return {'x': 0, 'y': 0}


def what_is_in_position(the_map, pos):
    '''Determines what is at the current postion on the map, wrapping along both axis when necessary'''
    return ''


def traverse_map_at_angle(the_map, start_pos, d_x, d_y):
    '''Traverses the map, repeating along the x axis only, outputting the number of open and tree spaces encountered'''
    return {'open': 0, 'tree': 0}


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day3.txt')
    print(lines)
