from typing import List


def is_multiple(a: int, b: int):
    return a % b == 0


def is_bigest_multiple(a: int, b: int):
    c = a // b
    return b * c


def is_prime(n: int):
    d = 2
    while n > d:
        if n % d == 0:
            return False
        d += 1
    return True


def bound_sqrt_2(digit: int) -> List[float]:
    val = 2
    step = 10**-digit
    x = 0
    y = 0
    while (x + step) ** 2 < val:
        x += step
    while y**2 < val:
        y += step
    return [round(x, digit), round(y, digit)]
