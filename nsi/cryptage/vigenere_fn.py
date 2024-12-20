from typing import List
from code_fn import is_derived_from_default_alphabet


def code_vigenere(alphabet: List[str], text: str, keyword: str):
    """Return the message encoded with Vigenere's key.

    text : str
    keyword : str

    return : str"""

    derived_from_default_alphabet = is_derived_from_default_alphabet(alphabet=alphabet)
    result = ""

    i = 0
    for character in text:
        if (
            character.lower() if derived_from_default_alphabet else character
        ) in alphabet:
            index = alphabet.index(
                character.lower() if derived_from_default_alphabet else character
            )
            offset = alphabet.index(
                keyword[i].lower() if derived_from_default_alphabet else keyword[i]
            )
            new_letter = alphabet[
                (
                    index + offset
                    if index + offset <= len(alphabet) - 1
                    else offset - len(alphabet) + index
                )
            ]
            result = result + (
                new_letter.upper()
                if character.isupper() and derived_from_default_alphabet
                else new_letter
            )

        else:
            result = result + character

        i = i + 1 if i < len(keyword) - 1 else 0

    return result


def decode_vigenere(alphabet: List[str], text: str, keyword: str):
    """Return the message decoded with Vigenere's key.

    text : str
    keyword : str

    return : str"""

    derived_from_default_alphabet = is_derived_from_default_alphabet(alphabet=alphabet)
    result = ""
    i = 0

    for character in text:
        if (
            character.lower() if derived_from_default_alphabet else character
        ) in alphabet:
            index = alphabet.index(
                character.lower() if derived_from_default_alphabet else character
            )
            offset = alphabet.index(
                keyword[i].lower() if derived_from_default_alphabet else keyword[i]
            )
            new_letter = alphabet[
                (
                    index - offset
                    if index - offset >= 0
                    else index - offset + len(alphabet)
                )
            ]
            result = result + (
                new_letter.upper()
                if character.isupper() and derived_from_default_alphabet
                else new_letter
            )

        else:
            result = result + character

        i = i + 1 if i < len(keyword) - 1 else 0

    return result
