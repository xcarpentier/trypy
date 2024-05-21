from random import *


def simulation_somme_3d():
    des = [1, 2, 3, 4, 5, 6]
    lancerDes1 = choice(des)
    lancerDes2 = choice(des)
    lancerDes3 = choice(des)
    somme = lancerDes1 + lancerDes2 + lancerDes3
    return somme


def fréquence9_10(N):
    somme9 = 0
    somme10 = 0
    for i in range(1, N + 1):
        somme = simulation_somme_3d()
        if somme == 9:
            somme9 = somme9 + 1
        elif somme == 10:
            somme10 = somme10 + 1
    frequence9 = somme9 / N
    frequence10 = somme10 / N
    return frequence9, frequence10


N = int(input("Donner le nombre de répétition de l'expérience, N = "))
f9, f10 = fréquence9_10(N)
print("Fréquence de la somme égale à 9 : ", f9)
print("Fréquence de la somme égale à 10 : ", f10)
