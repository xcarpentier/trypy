def dichotomie(a, b, l):
    """number, number, number -> number, number
    hypothèse: a, b >= 0
    Retourne un encadrement de la racine cubique de 2 avec une précision l"""
    while b - a > l:
        m = (a + b) / 2
        if m**3 < 2:
            a = m
        else:
            b = m
    return a, b
