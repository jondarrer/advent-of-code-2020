import d5part2


def test_first_missing_seat_id_from_boarding_passes():
    boarding_passes = ['FFFFFFBRRL', 'FFFFFFBRLR', 'FFFFFBFLLL']
    actual = d5part2.first_missing_seat_id_from_boarding_passes(
        boarding_passes)
    assert actual == 15
