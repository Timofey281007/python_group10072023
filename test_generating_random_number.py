import generating_random_number


def test_generate_random_number():
    assert 0 <= generating_random_number.generate_random_number() <= 1000
