from bilan_sequence_8 import *


def test_secante():
    assert est_secante(5, 4)


def test_non_secante():
    assert not est_secante(4, 4)


def test_sont_confondues():
    assert sont_confondues(1, 1, 2, 2)


def test_non_confondues():
    assert not sont_confondues(1, 2, 3, 4)


def test_point_intersection():
    assert point_intersection(3, 4, 5, 6)


def test_non_point_intersection():
    assert not point_intersection(3, 3, 5, 7)
