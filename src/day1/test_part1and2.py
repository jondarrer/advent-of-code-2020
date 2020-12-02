import part1and2


def test_find_unique_groups_from_entries_2_blank():
    entries = []
    actual = part1and2.find_unique_groups_from_entries(entries, 2)
    assert actual == []


def test_find_unique_groups_from_entries_2_one():
    entries = [1]
    actual = part1and2.find_unique_groups_from_entries(entries, 2)
    assert actual == []


def test_find_unique_groups_from_entries_2_two():
    entries = [1, 2]
    actual = part1and2.find_unique_groups_from_entries(entries, 2)
    assert actual == [[1, 2]]


def test_find_unique_groups_from_entries_2_three():
    entries = [1, 2, 3]
    actual = part1and2.find_unique_groups_from_entries(entries, 2)
    assert actual == [[1, 2], [1, 3], [2, 3]]


def test_find_unique_pairs_from_entries_2_with_duplicate():
    entries = [1, 2, 3, 2]
    actual = part1and2.find_unique_groups_from_entries(entries, 2)
    assert actual == [[1, 2], [1, 3], [1, 2], [2, 3], [2, 2], [3, 2]]


def test_find_unique_groups_from_entries_3_two():
    entries = [1, 2]
    actual = part1and2.find_unique_groups_from_entries(entries, 3)
    assert actual == []


def test_find_unique_groups_from_entries_3_three():
    entries = [1, 2, 3]
    actual = part1and2.find_unique_groups_from_entries(entries, 3)
    assert actual == [[1, 2, 3]]


def test_find_unique_groups_from_entries_3_with_duplicate():
    entries = [1, 2, 3, 2]
    actual = part1and2.find_unique_groups_from_entries(entries, 3)
    assert actual == [[1, 2, 3], [1, 2, 2], [1, 3, 2], [2, 3, 2]]


def test_filter_groups_by_target_sum_blank():
    groups = []
    actual = part1and2.filter_groups_by_target_sum(groups, 0)
    assert actual == []


def test_filter_groups_by_target_sum_2_one_none():
    pairs = [[1, 2]]
    actual = part1and2.filter_groups_by_target_sum(pairs, 4)
    assert actual == []


def test_filter_groups_by_target_sum_2_two_one():
    pairs = [[1, 2], [1, 3]]
    actual = part1and2.filter_groups_by_target_sum(pairs, 4)
    assert actual == [[1, 3]]


def test_filter_groups_by_target_sum_3_two_one():
    tuples = [[1, 2, 3]]
    actual = part1and2.filter_groups_by_target_sum(tuples, 6)
    assert actual == [[1, 2, 3]]


def test_filter_groups_by_target_sum_3_two_two():
    tuples = [[1, 2, 3], [2, 3, 4]]
    actual = part1and2.filter_groups_by_target_sum(tuples, 9)
    assert actual == [[2, 3, 4]]


def test_product_of_a_group_none():
    group = None
    actual = part1and2.product_of_a_group(group)
    assert actual == 0


def test_product_of_a_group_2_one():
    pair = []
    actual = part1and2.product_of_a_group(pair)
    assert actual == 0
    pair = [1]
    actual = part1and2.product_of_a_group(pair)
    assert actual == 0
    pair = [1, 2, 3]
    actual = part1and2.product_of_a_group(pair)
    assert actual == 0


def test_product_of_a_group_2_two():
    pair = [2, 3]
    actual = part1and2.product_of_a_group(pair)
    assert actual == 6


def test_product_of_a_group_3_one():
    tuple = []
    actual = part1and2.product_of_a_group(tuple)
    assert actual == 0
    tuple = [1]
    actual = part1and2.product_of_a_group(tuple)
    assert actual == 0
    tuple = [1, 2]
    actual = part1and2.product_of_a_group(tuple)
    assert actual == 0
    tuple = [1, 2, 3, 4]
    actual = part1and2.product_of_a_group(tuple)
    assert actual == 0


def test_product_of_a_group_3_two():
    tuple = [2, 3, 4]
    actual = part1and2.product_of_a_group(tuple)
    assert actual == 24


def test_find_product_of_groups_which_sum_to_target_2_1():
    expense_report = []
    target_sum = 0
    assert part1and2.find_product_of_groups_which_sum_to_target(
        expense_report, target_sum, 2) == 0


def test_find_product_of_groups_which_sum_to_target_2_2():
    expense_report = [1, 2]
    target_sum = 3
    assert part1and2.find_product_of_groups_which_sum_to_target(
        expense_report, target_sum, 2) == 2


def test_find_product_of_groups_which_sum_to_target_2_3():
    expense_report = [1721, 979, 366, 299, 675, 1456]
    target_sum = 2020
    assert part1and2.find_product_of_groups_which_sum_to_target(
        expense_report, target_sum, 2) == 514579


def test_find_product_of_groups_which_sum_to_target_3_1():
    expense_report = []
    target_sum = 0
    assert part1and2.find_product_of_groups_which_sum_to_target(
        expense_report, target_sum, 3) == 0


def test_find_product_of_groups_which_sum_to_target_3_2():
    expense_report = [2, 3, 4]
    target_sum = 9
    assert part1and2.find_product_of_groups_which_sum_to_target(
        expense_report, target_sum, 3) == 24


def test_find_product_of_groups_which_sum_to_target_3_3():
    expense_report = [1721, 979, 366, 299, 675, 1456]
    target_sum = 2020
    assert part1and2.find_product_of_groups_which_sum_to_target(
        expense_report, target_sum, 3) == 241861950
