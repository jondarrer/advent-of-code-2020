import d2part1


def test_is_password_valid_true_1():
    actual = d2part1.is_password_valid(1, 3, 'a', 'abcde')
    assert actual == True


def test_is_password_valid_true_2():
    actual = d2part1.is_password_valid(2, 9, 'c', 'ccccccccc')
    assert actual == True


def test_is_password_valid_false_1():
    actual = d2part1.is_password_valid(1, 3, 'b', 'cdefg')
    assert actual == False
