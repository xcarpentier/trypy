from random import choice, choices

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

n = int(input("Entrer le nombre de lettre à obtenir :"))
mot = ""
lettre = ""
for i in range(1, n + 1):
    lettre = choice(alphabet)
    mot = mot + lettre
print("Le mot obtenu est :", mot)

copie_alphabet = alphabet[:]
n = int(input("Entrer le nombre de lettre à obtenir :"))
mot = ""
lettre = ""
for i in range(1, n + 1):
    lettre = choice(copie_alphabet)
    mot = mot + lettre
    copie_alphabet.remove(lettre)
print("Le mot obtenu est :", mot)

urne = ["rouge", "rouge", "vert", "vert", "vert"]
print("La boule tirée est de couleur :", choice(urne))


def chance_simple(couleur_choisie, mise):
    issues = ["rouge", "noir", "vert"]
    effectifs = [18, 18, 2]
    couleur_sortie = choices(issues, effectifs)[0]
    if couleur_choisie == couleur_sortie:
        gain = mise
    else:
        gain = -mise
    return gain


choix = input("Choisissez votre couleur :")
mise = int(input("Choisissez votre mise :"))
print("Votre gain est de ", chance_simple(choix, mise), "euros.")
