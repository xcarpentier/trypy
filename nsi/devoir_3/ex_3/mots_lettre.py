from typing import List

tab_mots = ["banane", "pomme", "abricot", "beurre", "farine"]


def premiere_lettre(mots: List[str], lettre: str):
    for mot in mots:
        if mot[0] == lettre:
            print(mot)


premiere_lettre(tab_mots, "a")
