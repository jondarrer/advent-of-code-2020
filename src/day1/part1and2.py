from functools import reduce
import read_input_file


def find_unique_groups_from_entries(entries, size_of_group, level=-1):
    '''Finds unique groups of size size_of_group, from the list of entries'''
    if (level == -1):
        level = size_of_group
    if (level == 0):
        return []

    unique_groups = []
    for first_index in range(len(entries) - size_of_group + 1):
        for second_index in range(len(entries) - (first_index + size_of_group - 1)):
            if (size_of_group == 2):
                unique_groups.append(
                    [entries[first_index], entries[second_index + first_index + 1]])
            else:
                for third_index in range(len(entries) - (first_index + second_index + size_of_group - 1)):
                    unique_groups.append(
                        [entries[first_index], entries[second_index + first_index + 1], entries[first_index + second_index + third_index + size_of_group - 1]])

    return unique_groups
    # ents = find_unique_groups_from_entries(entries, size_of_group, level - 1)
    # ents.prepend()


def filter_groups_by_target_sum(groups, target_sum):
    '''Filters a list of pairs by the target_sum'''
    if (groups == None or len(groups) == 0):
        return []
    return list(filter((lambda group: reduce((lambda x, y: x + y), group) == target_sum), groups))


def product_of_a_group(group):
    '''Returns the product of a group, e.g. a group of [3, 4] would return 12'''
    if (group == None or len(group) == 0):
        return 0
    return reduce((lambda x, y: x * y), group)


def find_product_of_groups_which_sum_to_target(entries, target_sum, size_of_group):
    '''Returns the product of a group of entries of size size_of_group, which when summed match the target_sum'''
    if len(entries) == 0:
        return 0

    groups = filter_groups_by_target_sum(
        find_unique_groups_from_entries(entries, size_of_group), target_sum)
    print(groups)
    target_group_products = list(map(product_of_a_group, groups))

    if (len(target_group_products)) > 0:
        return target_group_products[0]


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
