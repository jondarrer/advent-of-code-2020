import read_input_file


def find_three_entries_which_sum_to_target_and_multiply(entries, target_sum):
    '''Returns the product of three entries which when summed match the target_sum'''
    if len(entries) == 0:
        return 0

    tuples = filter_tuples_by_target_sum(
        find_unique_tuples_from_entries(entries), target_sum)
    print(tuples)
    target_tuple_products = list(map(product_of_a_tuple, tuples))

    if (len(target_tuple_products)) > 0:
        return target_tuple_products[0]


def find_unique_tuples_from_entries(entries):
    '''Finds unique tuples from the list of entries'''
    if (entries == None or len(entries) < 3):
        return []

    unique_tuples = []
    for first_index in range(len(entries) - 2):
        for second_index in range(len(entries) - (first_index + 2)):
            for third_index in range(len(entries) - (first_index + second_index + 2)):
                unique_tuples.append(
                    [entries[first_index], entries[second_index + first_index + 1], entries[third_index + second_index + first_index + 2]])

    return unique_tuples


def filter_tuples_by_target_sum(tuples, target_sum):
    '''Filters a list of tuples by the target_sum'''
    return list(filter(lambda tuple: tuple[0] + tuple[1] + tuple[2] == target_sum, tuples))


def product_of_a_tuple(tuple):
    '''Returns the product of a tuple, e.g. a tuple of [3, 4] would return 12'''
    if (tuple == None or len(tuple) != 3):
        return 0

    return tuple[0] * tuple[1] * tuple[2]


if __name__ == '__main__':
    result = find_three_entries_which_sum_to_target_and_multiply(
        read_input_file.read(
            '/Users/jondarrer/Code/advent-of-code-2020/src/input/day1.txt'),
        2020
    )
    print(result)
