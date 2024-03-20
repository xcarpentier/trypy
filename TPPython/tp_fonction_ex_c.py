def f(xM, yM):
    """number, number -> boolean
    retourne le boolean True si le point M(xM, yM) est en dessous de
    la droite d'équation 3*xM-5
    """
    Vrai_ou_Faux = yM < 3 * xM - 5
    return Vrai_ou_Faux
