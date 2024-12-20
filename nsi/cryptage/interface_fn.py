from typing import List
from constants import ALPHABET, CUSTOM_ALPHABET, NONEXISTENT_OPTION


def get_option_choice():
    while True:
        option_choice: str = input(
            """1. Cryptage
2. Décryptage
3. Alphabet personnalisé

Choisissez une des options (tapez 1, 2 ou 3), ou n'entrez rien pour quitter : """
        )
        print("\n")

        if (
            option_choice == "1"
            or option_choice == "2"
            or option_choice == "3"
            or option_choice == ""
        ):
            break

        else:
            print(NONEXISTENT_OPTION)

    return option_choice


def get_code_key():
    while True:
        code_key = input(
            """1. ROT-13
2. ROT-47
3. César
4. Vigenère
5. Polybe

Choisissez la clé que vous souhaitez utiliser ou annulez (tapez 1, 2, 3 ou 4), ou n'entrez rien pour annuler : """
        )
        print("\n")

        if (
            code_key == "1"
            or code_key == "2"
            or code_key == "3"
            or code_key == "4"
            or code_key == "5"
            or code_key == ""
        ):
            break
        else:
            print(NONEXISTENT_OPTION)

    return code_key


def get_custom_alphabet():
    while True:
        CUSTOM_ALPHABET = input(
            "Entrez votre alphabet personnalisé sans mettre d'espaces entre les caractères et en faisant attention à ce qu'il n'y ait pas de doublons, ou n'entrez rien pour annuler : "
        )
        print("\n")

        valid_alphabet = True

        for character in CUSTOM_ALPHABET:
            if CUSTOM_ALPHABET.count(character) > 1:
                valid_alphabet = False
                break

        if valid_alphabet:
            break

        else:
            print("Il y avait un ou plusieurs doublons dans votre alphabet.\n")

    if CUSTOM_ALPHABET != "":
        CUSTOM_ALPHABET = list(CUSTOM_ALPHABET)

        print("Votre alphabet personnalisé a bien été enregistré.\n")


def get_alphabet_choice():
    while True:
        alphabet_choice = input(
            """1. Alphabet par défaut (a-z)
2. Alphabet ASCII"""
            + (
                """
3. Alphabet personnalisé"""
                if CUSTOM_ALPHABET
                else ""
            )
            + "\nChoisissez l'alphabet que vous voulez utiliser (n'entrez rien pour annuler) : "
        )

        if (
            alphabet_choice == "1"
            or alphabet_choice == "2"
            or (CUSTOM_ALPHABET and alphabet_choice == "3")
            or alphabet_choice == ""
        ):
            break

        else:
            print(NONEXISTENT_OPTION)

    return alphabet_choice


def get_alphabet_with_keyword_choice():
    while True:
        alphabet_with_keyword_choice = input(
            "Voulez-vous utiliser un alphabet avec un mot-clé ? (o/n, n'entrez rien pour annuler) : "
        )
        print("\n")

        if (
            alphabet_with_keyword_choice == "o"
            or alphabet_with_keyword_choice == "n"
            or alphabet_with_keyword_choice == ""
        ):
            break

        else:
            print(NONEXISTENT_OPTION)

    return alphabet_with_keyword_choice


def get_alphabet_keyword(alphabet: List[str]):
    while True:
        alphabet_keyword = input(
            "Entrez le mot-clé pour l'alphabet que vous avez choisi ou n'entrez rien pour annuler : "
        )

        valid_alphabet_keyword = True

        for character in alphabet_keyword:
            if (
                character.lower() if alphabet == ALPHABET else character
            ) not in alphabet or alphabet_keyword.count(character) > 1:
                valid_alphabet_keyword = False
                break

        if valid_alphabet_keyword:
            break

        else:
            print(NONEXISTENT_OPTION)

    return alphabet_keyword


def get_cesar_offset():
    while True:
        offset = input(
            "Entrez le décalage de lettre (ex. : 5), ou n'entrez rien pour annuler : "
        )
        print("\n")

        if offset.isdigit() or offset == "":
            break

        else:
            print(NONEXISTENT_OPTION)

    return offset


def get_vigenere_keyword(alphabet: List[str]):
    while True:
        keyword: str = input(
            "Entrez le mot clé (il ne doit contenir aucun caractère étranger à l'alphabet choisi), ou n'entrez rien pour annuler : "
        )
        print("\n")

        valid_keyword: bool = True

        for character in keyword:
            if (
                character.lower() if alphabet == ALPHABET else character
            ) not in alphabet:
                valid_keyword = False
                break

        if valid_keyword:
            break

        else:
            print(NONEXISTENT_OPTION)

    return keyword.lower()


def get_message():
    message = input(
        f"Entrez le message à crypter ou à décrypter ou n'entrez rien pour annuler : "
    )
    print("\n")

    return message
