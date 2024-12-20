from typing import List
from constants import ALPHABET


def generate_alphabet_with_keyword(alphabet: List[str], keyword: str):
    keyword_alphabet = []

    for character in keyword:
        if character not in keyword_alphabet:
            keyword_alphabet.append(character)

    for character in alphabet:
        if character not in keyword_alphabet:
            keyword_alphabet.append(character)

    return keyword_alphabet


def is_derived_from_default_alphabet(alphabet: List[str]):
    look_like_default_alphabet = True

    for character in alphabet:
        if character not in ALPHABET:
            look_like_default_alphabet = False
            break

    return look_like_default_alphabet
