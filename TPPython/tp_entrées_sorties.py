n = int(input("Donner un entier n, n = "))  # On demande d’entrer un entier.
est_pair = (
    n % 2 == 0
)  # On teste si cet entier est pair (si oui, le reste de sa division euclidienne par 2 est 0)
print(
    "L’entier ", n, " est pair, est une affirmation : ", est_pair, "."
)  # On affiche le résultat.
m = int(input("Donner un nombre m, m = "))  # On demande d'entrer un entier
print("La variable m est de type : ", type(m))  # On donne le type de la variable m
print(type(m))  # On donne le type de la variable m
print(
    "Attention ! m n’est pas de type number mais de type string."
)  # On dit que m est de type string pas de type number
reponse = input(
    "Répondre par oui ou non, m est un multiple de trois ? "
)  # On demande si m est multiple de 3
print("Votre réponse est ", reponse, ". Vérifions.")  # On donne valide la réponse
est_multiple_de_3 = m % 3 == 0  # On vérifie si m est multiple de 3
print(
    "L’entier ",
    m,
    " est un multiple de 3, est une affirmation : ",
    est_multiple_de_3,
    ".",
)  # On dit si m est multiple de 3

x = float(input("Donner un réel x :"))
print(x)

x = eval(input("Donner un réel x :"))
print(x)

# Entrées
poids = float(input("Entrer le poids en kg de riz à acheter : "))
# Traitement: calcul du prix à payer en euros
if poids <= 2:
    prix = 10 * poids
else:
    prix = 5 * poids + 10
# Sorties
print("Le prix à payer en euros est :", round(prix, 4))
