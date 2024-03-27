from random import choice


def effectif(n):
    piece = ["F", "P"]
    nb_face = 0
    for k in range(1, n + 1):
        lancer = choice(piece)
        if lancer == "F":
            nb_face = nb_face + 1
    return nb_face


def frequence(n):
    frequence = effectif(n) / n
    return frequence
