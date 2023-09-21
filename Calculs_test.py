from Calculs import is_multiple, is_bigest_multiple, is_prime, bound_sqrt_2
from math import sqrt, pow


def test_is_multiple():
    assert is_multiple(4, 2)


def test_is_not_multiple():
    assert not is_multiple(5, 2)


def test_is_biggest_multiple():
    assert is_bigest_multiple(5, 2) == 4


def test_is_prime():
    assert is_prime(108877)


def test_is_not_prime():
    assert not is_prime(123456789991)


def test_bound_sqrt_2_dyn():
    for x in range(3):
        assert bound_sqrt_2(x) == [
            round(sqrt(2), x),
            round(round(sqrt(2), x) + pow(10, -x), x),
        ]
