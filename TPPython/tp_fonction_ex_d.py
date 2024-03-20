def appartient_c(xM, yM):
    """number,number -> boolean
    Retourne le boolean True si le point M(xM,yM) appartient à la courbe d'équation 3*x-5
    """
    Vrai_ou_Faux = yM == 3 / xM - 5
    return Vrai_ou_Faux


from math import sqrt

print("Le point A appartient-il à la courbe C ?", appartient_c(1, -2))
print("Le point B appartient-il à la courbe C ?", appartient_c(-3, 2))
print(
    "Le point C appartient-il à la courbe C ?",
    appartient_c(sqrt(2), ((3 / sqrt(2)) - 5)),
)
