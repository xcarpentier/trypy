from math import sqrt


def Appartient_Cercle(x_A, y_A, R, x_B, y_B) -> bool:
    if sqrt((x_B - x_A) ** 2 + (y_B - y_A) ** 2) == R:
        return True
    else:
        return False


x_A = float(input("Donner la coordonnée x de A:"))
y_A = float(input("Donner la coordonnée y de A:"))
x_B = float(input("Donner la coordonnée x de B:"))
y_B = float(input("Donner la coordonnée y de B:"))
R = float(input("Donner le rayon R du cercle de centre A:"))
if Appartient_Cercle(x_A, y_A, R, x_B, y_B) == True:
    print("Le point B appartient au cercle de centre A et de rayon R.")
else:
    print("Le point B n'appartient pas au cercle de centre A et de rayon R.")
