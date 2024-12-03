from typing import List

tab_mots = ["banane", "pomme", "abricot", "beurre", "farine"]


def nombre(mots: List[str], lettre: str):
    nombre_mots = 0
    for mot in mots:
        if mot[0] == lettre:
            nombre_mots += 1
    return nombre_mots


print(nombre(tab_mots, "p"))
