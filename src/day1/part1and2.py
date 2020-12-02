import read_input_file


def find_unique_groups_from_entries(entries, size_of_group):
    '''Finds unique groups of size size_of_group, from the list of entries'''
    return []


def filter_groups_by_target_sum(groups, target_sum):
    '''Filters a list of pairs by the target_sum'''
    return []


def product_of_a_group(group):
    '''Returns the product of a group, e.g. a group of [3, 4] would return 12'''
    return 0


def find_product_of_groups_which_sum_to_target(entries, target_sum, size_of_group):
    '''Returns the product of a group of entries of size size_of_group, which when summed match the target_sum'''
    return 0


if __name__ == '__main__':
    result = find_product_of_groups_which_sum_to_target(
        read_input_file.read(
            '/Users/jondarrer/Code/advent-of-code-2020/src/input/day1.txt'),
        2020,
        2
    )
    print('part1', result)

    result = find_product_of_groups_which_sum_to_target(
        read_input_file.read(
            '/Users/jondarrer/Code/advent-of-code-2020/src/input/day1.txt'),
        2020,
        3
    )
    print('part2', result)
