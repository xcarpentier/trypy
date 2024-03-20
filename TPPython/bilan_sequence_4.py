from typing import Tuple

# Exemple de dico
# dico = {"x": 1, "y": 2}
# print(dico["x"])
# print(dico["y"])

X = float
Y = float


def coordonnees_vecteurs(x_A, y_A, x_B, y_B) -> Tuple[X, Y]:
    x = x_B - x_A
    y = y_B - y_A
    return (x, y)


def sont_alignes(coordA: Tuple[X, Y], coordB: Tuple[X, Y], coordC: Tuple[X, Y]):
    AB = coordonnees_vecteurs(coordA[0], coordA[1], coordB[0], coordB[1])
    AC = coordonnees_vecteurs(coordA[0], coordA[1], coordC[0], coordC[1])
    if AB[0] * AC[1] - AB[1] * AC[0] == 0:
        return True
    else:
        return False


x_A = float(input("Coordonnée x de A:"))
y_A = float(input("Coordonnée y de A:"))
x_B = float(input("Coordonnée x de B:"))
y_B = float(input("Coordonnée y de B:"))
x_C = float(input("Coordonnée x de C:"))
y_C = float(input("Coordonnée y de C:"))
if sont_alignes((x_A, y_A), (x_B, y_B), (x_C, y_C)) == True:
    print("Les points A, B et C sont alignés.")
else:
    print("Les points A, B et C ne sont pas alignés.")
