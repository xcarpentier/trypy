Tab = [
    ["Bel Hair", 2546972642, 26989, 85697],
    ["DoneTsou", 2555872541, 16235, 45689628],
    ["Chiffon&Co", 9872822489, 35604, 652571],
    ["Bul2gum", 4783654829, 4560, 25231],
]

for element in Tab:
    element.append(element[3] / 10)

for element in Tab:
    print(
        f"""Nom de l'entreprise : {element[0]}
Numéro SIRET : {element[1]}
Montant estimé des dégradations : {element[2]} €
Chiffre d'affaires : {element[3]} €
10% : {element[4]}
"""
    )
