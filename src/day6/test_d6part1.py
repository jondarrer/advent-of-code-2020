import d6part1


def test_number_of_unique_answers_per_group_1():
    answers = ['abc']
    actual = d6part1.number_of_unique_answers_per_group(answers)
    assert actual == 3


def test_number_of_unique_answers_per_group_2():
    answers = ['a', 'b', 'c']
    actual = d6part1.number_of_unique_answers_per_group(answers)
    assert actual == 3


def test_number_of_unique_answers_per_group_3():
    answers = ['ab', 'ac']
    actual = d6part1.number_of_unique_answers_per_group(answers)
    assert actual == 3


def test_number_of_unique_answers_per_group_4():
    answers = ['a', 'a', 'a', 'a']
    actual = d6part1.number_of_unique_answers_per_group(answers)
    assert actual == 1


def test_number_of_unique_answers_per_group_5():
    answers = ['b']
    actual = d6part1.number_of_unique_answers_per_group(answers)
    assert actual == 1


def test_total_number_of_unique_answers():
    all_group_answers = []
    actual = d6part1.total_number_of_unique_answers(all_group_answers)
    assert actual == 11
