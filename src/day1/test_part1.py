import part1


def test_find_two_entries_which_sum_to_target_and_multiply():
    expense_report = [1721, 979, 366, 299, 675, 1456]
    target_sum = 2020
    assert part1.find_two_entries_which_sum_to_target_and_multiply(
        expense_report, target_sum) == 514579
