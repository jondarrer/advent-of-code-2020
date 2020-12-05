import d4part2


def test_is_passport_valid_false_1():
    passport = 'eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926'
    actual = d4part2.is_passport_valid(passport)
    assert actual == False


def test_is_passport_valid_false_2():
    passport = 'iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946'
    actual = d4part2.is_passport_valid(passport)
    assert actual == False


def test_is_passport_valid_false_3():
    passport = 'hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277'
    actual = d4part2.is_passport_valid(passport)
    assert actual == False


def test_is_passport_valid_false_4():
    passport = 'hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007'
    actual = d4part2.is_passport_valid(passport)
    assert actual == False


def test_is_passport_valid_true_1():
    passport = 'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f'
    actual = d4part2.is_passport_valid(passport)
    assert actual == True


def test_is_passport_valid_true_2():
    passport = 'eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm'
    actual = d4part2.is_passport_valid(passport)
    assert actual == True


def test_is_passport_valid_true_3():
    passport = 'hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022'
    actual = d4part2.is_passport_valid(passport)
    assert actual == True


def test_is_passport_valid_true_4():
    passport = 'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'
    actual = d4part2.is_passport_valid(passport)
    assert actual == True


def test_is_byr_valid_false_1():
    byr = '1919'
    actual = d4part2.is_byr_valid(byr)
    assert actual == False


def test_is_byr_valid_false_2():
    byr = '2003'
    actual = d4part2.is_byr_valid(byr)
    assert actual == False


def test_is_byr_valid_true_1():
    byr = '1977'
    actual = d4part2.is_byr_valid(byr)
    assert actual == True


def test_is_iyr_valid_false_1():
    iyr = '2009'
    actual = d4part2.is_iyr_valid(iyr)
    assert actual == False


def test_is_iyr_valid_false_2():
    iyr = '2021'
    actual = d4part2.is_iyr_valid(iyr)
    assert actual == False


def test_is_iyr_valid_true_1():
    iyr = '2014'
    actual = d4part2.is_iyr_valid(iyr)
    assert actual == True


def test_is_eyr_valid_false_1():
    eyr = '2019'
    actual = d4part2.is_eyr_valid(eyr)
    assert actual == False


def test_is_eyr_valid_false_2():
    eyr = '2031'
    actual = d4part2.is_eyr_valid(eyr)
    assert actual == False


def test_is_eyr_valid_true_1():
    eyr = '2021'
    actual = d4part2.is_eyr_valid(eyr)
    assert actual == True


def test_is_hgt_valid_missing_false_1():
    hgt = '180'
    actual = d4part2.is_hgt_valid(hgt)
    assert actual == False


def test_is_hgt_valid_missing_false_2():
    hgt = '70'
    actual = d4part2.is_hgt_valid(hgt)
    assert actual == False


def test_is_hgt_valid_cm_false_1():
    hgt = '149cm'
    actual = d4part2.is_hgt_valid(hgt)
    assert actual == False


def test_is_hgt_valid_cm_false_2():
    hgt = '194cm'
    actual = d4part2.is_hgt_valid(hgt)
    assert actual == False


def test_is_hgt_valid_cm_true_1():
    hgt = '180cm'
    actual = d4part2.is_hgt_valid(hgt)
    assert actual == True


def test_is_hgt_valid_in_false_1():
    hgt = '58in'
    actual = d4part2.is_hgt_valid(hgt)
    assert actual == False


def test_is_hgt_valid_in_false_2():
    hgt = '77in'
    actual = d4part2.is_hgt_valid(hgt)
    assert actual == False


def test_is_hgt_valid_in_true_1():
    hgt = '70in'
    actual = d4part2.is_hgt_valid(hgt)
    assert actual == True


def test_is_hcl_valid_false_1():
    hcl = '#00fffg'
    actual = d4part2.is_hcl_valid(hcl)
    assert actual == False


def test_is_hcl_valid_false_2():
    hcl = '#00fffff'
    actual = d4part2.is_hcl_valid(hcl)
    assert actual == False


def test_is_hcl_valid_true_1():
    hcl = '#00ffff'
    actual = d4part2.is_hcl_valid(hcl)
    assert actual == True


def test_is_ecl_valid_false_1():
    ecl = 'ambr'
    actual = d4part2.is_ecl_valid(ecl)
    assert actual == False


def test_is_ecl_valid_true_1():
    ecl = 'amb'
    actual = d4part2.is_ecl_valid(ecl)
    assert actual == True


def test_is_ecl_valid_true_2():
    ecl = 'blu'
    actual = d4part2.is_ecl_valid(ecl)
    assert actual == True


def test_is_ecl_valid_true_3():
    ecl = 'brn'
    actual = d4part2.is_ecl_valid(ecl)
    assert actual == True


def test_is_ecl_valid_true_4():
    ecl = 'gry'
    actual = d4part2.is_ecl_valid(ecl)
    assert actual == True


def test_is_ecl_valid_true_5():
    ecl = 'grn'
    actual = d4part2.is_ecl_valid(ecl)
    assert actual == True


def test_is_ecl_valid_true_6():
    ecl = 'hzl'
    actual = d4part2.is_ecl_valid(ecl)
    assert actual == True


def test_is_ecl_valid_true_7():
    ecl = 'oth'
    actual = d4part2.is_ecl_valid(ecl)
    assert actual == True


def test_is_pid_valid_false_1():
    pid = '00000000a'
    actual = d4part2.is_pid_valid(pid)
    assert actual == False


def test_is_pid_valid_false_2():
    pid = '00000000'
    actual = d4part2.is_pid_valid(pid)
    assert actual == False


def test_is_pid_valid_true_1():
    pid = '123456789'
    actual = d4part2.is_pid_valid(pid)
    assert actual == True


def test_how_many_passports_are_valid():
    passport_1 = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'
    passport_2 = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929'
    passport_3 = 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'
    passport_4 = 'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'
    actual = d4part2.how_many_passports_are_valid(
        [passport_1, passport_2, passport_3, passport_4])
    assert actual == 2
