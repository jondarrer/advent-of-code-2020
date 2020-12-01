import part1


def test_find_unique_pairs_from_entries_blank():
    entries = []
    actual = part1.find_unique_pairs_from_entries(entries)
    assert actual == []


def test_find_unique_pairs_from_entries_one():
    entries = [1]
    actual = part1.find_unique_pairs_from_entries(entries)
    assert actual == []


def test_find_unique_pairs_from_entries_two():
    entries = [1, 2]
    actual = part1.find_unique_pairs_from_entries(entries)
    assert actual == [[1, 2]]


def test_find_unique_pairs_from_entries_three():
    entries = [1, 2, 3]
    actual = part1.find_unique_pairs_from_entries(entries)
    assert actual == [[1, 2], [1, 3], [2, 3]]


def test_find_unique_pairs_from_entries_with_duplicate():
    entries = [1, 2, 3, 2]
    actual = part1.find_unique_pairs_from_entries(entries)
    assert actual == [[1, 2], [1, 3], [1, 2], [2, 3], [2, 2], [3, 2]]


def test_filter_pairs_by_target_sum_blank():
    pairs = []
    actual = part1.filter_pairs_by_target_sum(pairs, 0)
    assert actual == []


def test_filter_pairs_by_target_sum_one_none():
    pairs = [[1, 2]]
    actual = part1.filter_pairs_by_target_sum(pairs, 4)
    assert actual == []


def test_filter_pairs_by_target_sum_two_one():
    pairs = [[1, 2], [1, 3]]
    actual = part1.filter_pairs_by_target_sum(pairs, 4)
    assert actual == [[1, 3]]


def test_product_of_a_pair_none():
    pair = None
    actual = part1.product_of_a_pair(pair)
    assert actual == 0


def test_product_of_a_pair_one():
    pair = []
    actual = part1.product_of_a_pair(pair)
    assert actual == 0
    pair = [1]
    actual = part1.product_of_a_pair(pair)
    assert actual == 0
    pair = [1, 2, 3]
    actual = part1.product_of_a_pair(pair)
    assert actual == 0


def test_product_of_a_pair_two():
    pair = [2, 3]
    actual = part1.product_of_a_pair(pair)
    assert actual == 6


def test_find_two_entries_which_sum_to_target_and_multiply_1():
    expense_report = []
    target_sum = 0
    assert part1.find_two_entries_which_sum_to_target_and_multiply(
        expense_report, target_sum) == 0


def test_find_two_entries_which_sum_to_target_and_multiply_2():
    expense_report = [1, 2]
    target_sum = 3
    assert part1.find_two_entries_which_sum_to_target_and_multiply(
        expense_report, target_sum) == 2


def test_find_two_entries_which_sum_to_target_and_multiply_3():
    expense_report = [1721, 979, 366, 299, 675, 1456]
    target_sum = 2020
    assert part1.find_two_entries_which_sum_to_target_and_multiply(
        expense_report, target_sum) == 514579
