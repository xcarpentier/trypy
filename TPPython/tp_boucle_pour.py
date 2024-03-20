# Entrées
N = int(input("Donner un entier naturel : N = "))  # Demande un nombre naturel
# Traitement
S = 0  # Ajoute une variable S = 0
for n in range(1, N + 1):
    print(S, " ", n)
    S = S + n
# Sorties
print("Le résultat est :", S)
