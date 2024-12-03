hauteur = 500
temps = 0

for hauteur in range(hauteur, 0, -20):
    hauteur -= 20
    temps += 1
    print(f"Au bout de {temps} secondes, vous êtes à {hauteur} mètres.")
