def est_secante(m1, m2):
    """number, number -> boolean
    Prend pour paramètres m1 et m2.
    Retourne le boolean True si les droites d'équation
     réduite y=m1x+p1 et y=m2x+p2 sont sécantes."""
    return m1 != m2


def sont_confondues(m1, m2, p1, p2):
    """"""
    return m1 == m2 and p1 == p2


def point_intersection(m1, m2, p1, p2):
    if est_secante(m1, m2):
        x = (p2 - p1) / (m1 - m2)
        y = (m1 * p2 - m2 * p1) / (m1 - m2)
        return x, y


m1 = float(input("Entrez m1 :"))
m2 = float(input("Entrez m2 :"))
p1 = float(input("Entrez p1 :"))
p2 = float(input("Entrez p2 :"))
if est_secante(m1, m2) == True:
    pi = point_intersection(m1, m2, p1, p2)
    print("Les droites sont sécantes en : ", pi)
elif sont_confondues(m1, m2, p1, p2) == True:
    print("Les droites sont confondues")
else:
    print("Les droites sont parallèles non confondues")
