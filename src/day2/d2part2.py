import read_input_file


def is_password_invalid(p1, p2, char, password):
    c1 = password[p1 - 1]
    c2 = password[p2 - 1]
    if (c1 == char and c2 == char):
        return False
    if (c1 != char and c2 != char):
        return False
    return True


def number_of_invalid_passwords(list_of_password_and_policy):
    valids = 0
    for password_and_policy in list_of_password_and_policy:
        if (is_password_invalid(
            int(password_and_policy['min']),
            int(password_and_policy['max']),
            password_and_policy['char'],
                password_and_policy['password']) == True):
            valids = valids + 1

    return valids


if __name__ == '__main__':
    list_of_password_and_policy = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day2.txt')
    print(number_of_invalid_passwords(list_of_password_and_policy))
