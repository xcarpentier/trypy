from math import ceil


def mediane(list) -> float:
    list.sort()
    eff = len(list)
    if eff % 2 == 0:
        med = (list[int(eff / 2) - 1] + list[int(eff / 2 + 1) - 1]) / 2
    else:
        med = list[int((eff + 1) / 2) - 1]
    return med


def quartiles(list) -> tuple:
    list.sort()
    eff = len(list)
    q1 = list[ceil(eff * 0.25) - 1]
    q3 = list[ceil(eff * 0.75) - 1]
    return q1, q3


L = []
element = input("Entrer un nombre entier, taper n pour terminer: ")
while element != "n":
    element = int(element)
    L.append(element)
    element = input("Entrer un nombre entier, taper n pour terminer: ")
Me = mediane(L)
Q1, Q3 = quartiles(L)
L.sort()
print("La liste ordonnée est ", L)
print("La médiane est Me = ", Me, ", les quartiles sont Q1 = ", Q1, " et Q3 = ", Q3)
