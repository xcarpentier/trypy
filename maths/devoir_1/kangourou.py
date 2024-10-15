from random import random


def traverse():
    x = 0
    for i in range(10):
        if x < 12:
            saut = random()
            if saut < 1 / 3:
                x = x + 2
            elif saut < 2 / 3:
                x = x + 1
            else:
                x = x - 1
    if x >= 12:
        return 1
    else:
        return 0


def prob_traverse(n):
    nbre_reussite = 0
    for i in range(n):
        nbre_reussite = nbre_reussite + traverse()
    return nbre_reussite / n
