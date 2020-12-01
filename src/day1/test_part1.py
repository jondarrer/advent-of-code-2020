import part1


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
