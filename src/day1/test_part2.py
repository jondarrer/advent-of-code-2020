import part2


def test_find_unique_tuples_from_entries_blank():
    entries = []
    actual = part2.find_unique_tuples_from_entries(entries)
    assert actual == []


def test_find_unique_tuples_from_entries_one():
    entries = [1]
    actual = part2.find_unique_tuples_from_entries(entries)
    assert actual == []


def test_find_unique_tuples_from_entries_two():
    entries = [1, 2]
    actual = part2.find_unique_tuples_from_entries(entries)
    assert actual == []


def test_find_unique_tuples_from_entries_three():
    entries = [1, 2, 3]
    actual = part2.find_unique_tuples_from_entries(entries)
    assert actual == [[1, 2, 3]]


def test_find_unique_tuples_from_entries_with_duplicate():
    entries = [1, 2, 3, 2]
    actual = part2.find_unique_tuples_from_entries(entries)
    assert actual == [[1, 2, 3], [1, 2, 2], [1, 3, 2], [2, 3, 2]]


def test_filter_tuples_by_target_sum_blank():
    tuples = []
    actual = part2.filter_tuples_by_target_sum(tuples, 0)
    assert actual == []


def test_filter_tuples_by_target_sum_two_one():
    tuples = [[1, 2, 3]]
    actual = part2.filter_tuples_by_target_sum(tuples, 6)
    assert actual == [[1, 2, 3]]


def test_filter_tuples_by_target_sum_two_two():
    tuples = [[1, 2, 3], [2, 3, 4]]
    actual = part2.filter_tuples_by_target_sum(tuples, 9)
    assert actual == [[2, 3, 4]]


def test_product_of_a_tuple_none():
    tuple = None
    actual = part2.product_of_a_tuple(tuple)
    assert actual == 0


def test_product_of_a_tuple_one():
    tuple = []
    actual = part2.product_of_a_tuple(tuple)
    assert actual == 0
    tuple = [1]
    actual = part2.product_of_a_tuple(tuple)
    assert actual == 0
    tuple = [1, 2]
    actual = part2.product_of_a_tuple(tuple)
    assert actual == 0
    tuple = [1, 2, 3, 4]
    actual = part2.product_of_a_tuple(tuple)
    assert actual == 0


def test_product_of_a_tuple_two():
    tuple = [2, 3, 4]
    actual = part2.product_of_a_tuple(tuple)
    assert actual == 24


def test_find_three_entries_which_sum_to_target_and_multiply_1():
    expense_report = []
    target_sum = 0
    assert part2.find_three_entries_which_sum_to_target_and_multiply(
        expense_report, target_sum) == 0


def test_find_three_entries_which_sum_to_target_and_multiply_2():
    expense_report = [2, 3, 4]
    target_sum = 9
    assert part2.find_three_entries_which_sum_to_target_and_multiply(
        expense_report, target_sum) == 24


def test_find_three_entries_which_sum_to_target_and_multiply_3():
    expense_report = [1721, 979, 366, 299, 675, 1456]
    target_sum = 2020
    assert part2.find_three_entries_which_sum_to_target_and_multiply(
        expense_report, target_sum) == 241861950
