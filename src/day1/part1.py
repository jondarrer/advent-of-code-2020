import read_input_file


def find_two_entries_which_sum_to_target_and_multiply(entries, target_sum):
    '''Returns the product of two entries which when summed match the target_sum'''
    if len(entries) == 0:
        return 0

    pairs = filter_pairs_by_target_sum(
        find_unique_pairs_from_entries(entries), target_sum)
    target_pair_products = list(map(product_of_a_pair, pairs))
    print(pairs)

    if (len(target_pair_products)) > 0:
        return target_pair_products[0]


def find_unique_pairs_from_entries(entries):
    '''Finds unique pairs from the list of entries'''
    if (entries == None or len(entries) < 2):
        return []

    unique_pairs = []
    for first_index in range(len(entries) - 1):
        for second_index in range(len(entries) - (first_index + 1)):
            unique_pairs.append(
                [entries[first_index], entries[second_index + first_index + 1]])

    return unique_pairs


def filter_pairs_by_target_sum(pairs, target_sum):
    '''Filters a list of pairs by the target_sum'''
    return list(filter(lambda pair: pair[0] + pair[1] == target_sum, pairs))


def product_of_a_pair(pair):
    '''Returns the product of a pair, e.g. a pair of [3, 4] would return 12'''
    if (pair == None or len(pair) != 2):
        return 0

    return pair[0] * pair[1]


if __name__ == '__main__':
    result = find_two_entries_which_sum_to_target_and_multiply(
        read_input_file.read(
            '/Users/jondarrer/Code/advent-of-code-2020/src/input/day1.txt'),
        2020
    )
    print(result)
