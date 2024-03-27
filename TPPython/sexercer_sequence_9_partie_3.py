def effectif(n):
    from random import random

    nb_R = 0
    for j in range(1, n + 1):
        res_tirage = random()
        if res_tirage <= 0.84:
            nb_R = nb_R + 1
    return nb_R


def frequence(n):
    eff = effectif(n)
    freq = eff / n
    return freq


def frequence_2(n, p):
    from random import random

    nb_B = 0
    for _ in range(1, n + 1):
        res_tirage = random()
        if res_tirage <= p:
            nb_B = nb_B + 1
    f = nb_B / n
    return f


def dedans(N, n, p):
    from math import sqrt

    nb_f = 0
    for _ in range(1, N + 1):
        f = frequence_2(n, p)
        if abs(p - f) <= 1 / sqrt(n):
            nb_f = nb_f + 1
    proportion = nb_f / N
    return proportion
