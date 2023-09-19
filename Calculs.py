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
