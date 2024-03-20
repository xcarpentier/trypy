# Traitement
n = 0
u = 1
while u < 1000:
    n = n + 1
    u = 2 * u
print("La puissance cherchée est :", n)
# Sorties

# Traitement
n = 0
u = 1
seuil = float(input("Donner un entier seuil:"))
while u > seuil:
    n = n + 1
    u = 0.8 * u
# Sorties
print("La puissance cherchée est : 0,8 puissance", n)
