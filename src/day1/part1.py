def find_two_entries_which_sum_to_target_and_multiply(entries, target_sum):
    '''Returns the product of two entries which when summed match the target_sum'''
    if len(entries) == 0:
        return 0

    target_pair_products = map(product_of_a_pair, filter_pairs_by_target_sum(
        find_unique_pairs_from_entries(entries), target_sum))

    if (len(target_pair_products)) > 0:
        return target_pair_products[0]


def find_unique_pairs_from_entries(entries):
    '''Finds unique pairs from the list of entries'''
    return []


def filter_pairs_by_target_sum(pairs, target_sum):
    '''Filters a list of pairs by the target_sum'''
    return []


def product_of_a_pair(pair):
    '''Returns the product of a pair, e.g. a pair of [3, 4] would return 12'''
    return 0
