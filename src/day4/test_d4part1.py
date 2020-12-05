import d4part1


def test_is_passport_valid_1():
    passport = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'
    actual = d4part1.is_passport_valid(passport)
    assert actual == True


def test_is_passport_valid_2():
    passport = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929'
    actual = d4part1.is_passport_valid(passport)
    assert actual == False


def test_is_passport_valid_3():
    passport = 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'
    actual = d4part1.is_passport_valid(passport)
    assert actual == True


def test_is_passport_valid_4():
    passport = 'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'
    actual = d4part1.is_passport_valid(passport)
    assert actual == False


def test_does_passport_have_field_1():
    passport = 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'
    actual = d4part1.does_passport_have_field(passport, 'hcl')
    assert actual == True


def test_does_passport_have_field_2():
    passport = 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'
    actual = d4part1.does_passport_have_field(passport, 'cid')
    assert actual == False


def test_how_many_passports_are_valid():
    passport_1 = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'
    passport_2 = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929'
    passport_3 = 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'
    passport_4 = 'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'
    actual = d4part1.how_many_passports_are_valid(
        [passport_1, passport_2, passport_3, passport_4])
    assert actual == 2
