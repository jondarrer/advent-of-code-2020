import d6part2


def test_number_of_answers_which_all_answered_1():
    answers = ['abc']
    actual = d6part2.number_of_answers_which_all_answered(answers)
    assert actual == 3


def test_number_of_answers_which_all_answered_2():
    answers = ['a', 'b', 'c']
    actual = d6part2.number_of_answers_which_all_answered(answers)
    assert actual == 0


def test_number_of_answers_which_all_answered_3():
    answers = ['ab', 'ac']
    actual = d6part2.number_of_answers_which_all_answered(answers)
    assert actual == 1


def test_number_of_answers_which_all_answered_4():
    answers = ['a', 'a', 'a', 'a']
    actual = d6part2.number_of_answers_which_all_answered(answers)
    assert actual == 1


def test_number_of_answers_which_all_answered_5():
    answers = ['b']
    actual = d6part2.number_of_answers_which_all_answered(answers)
    assert actual == 1


def test_total_number_of_answers_which_all_answered():
    all_group_answers = [['abc'], ['a', 'b', 'c'],
                         ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]
    actual = d6part2.total_number_of_answers_which_all_answered(
        all_group_answers)
    assert actual == 6
