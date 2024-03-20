def moyenne(list) -> float:
    """list -> float
    Prend en entrée une liste de valeur et en retourne la moyenne"""
    moy = sum(list) / len(list)
    return moy


def moyenne_pondérée(list_valeur, list_effectif) -> float:
    """list,list -> float
    Prend en entrée une liste de valeur et une liste d'effectifs et retourne la moyenne des valeurs pondérées par les effectifs
    """
    moy = 0
    for i in range(0, len(list_valeur)):
        moy = moy + list_valeur[i] * list_effectif[i]
    moy = moy / sum(list_effectif)
    return moy


def statistiques(valeur, effectif):
    """list,list -> number, number, number
    Prend en entrée les listes des valeurs et des effectifs d'une série statistiques,
     retourne :
     - la moyenne m des valeurs pondérées par les effectifs de la série
     - l'écart-type s de la série
     - la proportion p d'éléments appartenant à l'intervalle [m-2s,m+2s]"""

    from math import sqrt

    effectif_total = sum(effectif)
    nombre_de_valeur = len(valeur)

    m = 0
    v = 0
    for n in range(0, nombre_de_valeur):
        frequence = effectif[n] / effectif_total
        m = m + frequence * valeur[n]
        v = v + frequence * valeur[n] ** 2
    s = sqrt(v - m**2)

    p = 0
    for index in range(0, nombre_de_valeur):
        val = valeur[index]
        if val >= m - 2 * s and val <= m + 2 * s:
            p = p + effectif[index]
    p = p / effectif_total
    return m, s, p


# liste = [1, 3, 1, 2, 4, 1, 3, 6, 5, 2, 2, 1, 3, 0, 1, 2, 3, 3, 4, 1, 4]
# Moy = moyenne(liste)
# print(Moy)

# liste_valeur = [0, 1, 2, 3, 4, 5, 6]
# liste_effectif = [1, 6, 4, 5, 3, 1, 1]
# Moy = moyenne_pondérée(liste_valeur, liste_effectif)
# print(Moy)


liste_valeur = [0, 1, 2, 3, 4, 5, 6]
liste_effectif = [1, 6, 4, 5, 3, 1, 1]
m, s, p = statistiques(liste_valeur, liste_effectif)
print(m, s, p)
