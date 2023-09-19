from Calculs import is_multiple, is_bigest_multiple, is_prime


def test_is_multiple():
    assert is_multiple(4, 2)


def test_is_not_multiple():
    assert not is_multiple(5, 2)


def test_is_biggest_multiple():
    assert is_bigest_multiple(5, 2) == 4


def test_is_prime():
    assert is_prime(7)


def test_is_not_prime():
    assert not is_prime(12)
