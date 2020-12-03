import d2part2


def test_is_password_valid_true_1():
    actual = d2part2.is_password_invalid(1, 3, 'a', 'abcde')
    assert actual == True


def test_is_password_valid_false_1():
    actual = d2part2.is_password_invalid(1, 3, 'b', 'cdefg')
    assert actual == False


def test_is_password_valid_false_2():
    actual = d2part2.is_password_invalid(2, 9, 'c', 'ccccccccc')
    assert actual == False
