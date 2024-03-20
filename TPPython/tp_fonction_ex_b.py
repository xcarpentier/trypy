def fpy(x):
    """number -> float
    hypothèse: 5*x+1>=0
    retourne une valeur approchée de f(x)=3*x**2+sqrt(5x+1) pour x un nombre donné"""
    from math import sqrt

    y = -3 * x**2 + sqrt(5 * x + 1)
    return y


def test_fpy_1():
    assert fpy(0) == 1


def test_fpy_2():
    assert fpy(3) == 1
