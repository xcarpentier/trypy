from typing import List

Tab = [
    ["Bel Hair", 2546972642, 26989, 85697, 8569.7],
    ["DoneTsou", 2555872541, 16235, 45689628, 4568962.8],
    ["Chiffon&Co", 9872822489, 35604, 652571, 65257.1],
    ["Bul2gum", 4783654829, 4560, 25231, 2523.1],
    ["LeBarDesCopains", 2684887456, 5632, 168456, 16845.6],
]


def indemnite(entreprise: List):
    return entreprise[4] < entreprise[2]


# print(indemnite(Tab[4]))


def beneficiaires(listEntreprises: List):
    for entreprise in listEntreprises:
        if indemnite(entreprise):
            print(entreprise[1])


# beneficiaires(Tab)

nom = input("Entrez le nom de l'entreprise : ")

siret = ""
while len(siret) != 10 or siret.isdigit() != True:
    siret = input(
        "Entrez le numéro SIRET de l'entreprise (nombre entier à dix chiffres) : "
    )

montant_degats = ""
while not montant_degats.isdigit():
    montant_degats = input(
        "Entrez l'estimation du montant des dégradations de l'entreprise (nombre décimal) : "
    )

chiffre_affaires = ""
while not chiffre_affaires.isdigit():
    chiffre_affaires = input(
        "Entrez le chiffre d'affaires de l'entreprise (nombre décimal) : "
    )

Tab.append(
    [
        nom,
        int(siret),
        int(montant_degats),
        int(chiffre_affaires),
        round(int(chiffre_affaires) * 0, 1),
    ]
)

beneficiaires(Tab)
