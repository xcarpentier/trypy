from typing import List
from code_fn import is_derived_from_default_alphabet


def code_cesar_rot_13_rot_47(text: str, alphabet: List[str], offset: int):
    """
    Return the message entered encoded or decoded with ROT-13 key if the offset and the alphabet are not given, or coded with Cesar key if it is.

    text : str
    offset: int = 13

    return : str
    """

    derived_from_default_alphabet = is_derived_from_default_alphabet(alphabet=alphabet)
    result = ""

    for character in text:
        if (
            character.lower() if derived_from_default_alphabet else character
        ) in alphabet:
            index = alphabet.index(
                character.lower() if derived_from_default_alphabet else character
            )
            new_letter = alphabet[
                (
                    index + offset
                    if index + offset <= len(alphabet) - 1
                    else (index + offset) % len(alphabet)
                )
            ]
            result = result + (
                new_letter.upper()
                if character.isupper() and derived_from_default_alphabet
                else new_letter
            )

        else:
            result = result + character

    return result


def decode_cesar(alphabet: List[str], text: str, offset: int):
    """Return the message decoded with Cesar key.

    text: str
    offset: int

    return: str"""

    derived_from_default_alphabet = is_derived_from_default_alphabet(alphabet=alphabet)
    result = ""

    for character in text:
        if (
            character.lower() if derived_from_default_alphabet else character
        ) in alphabet:
            index = alphabet.index(
                character.lower() if derived_from_default_alphabet else character
            )
            new_letter = alphabet[
                (
                    index - offset
                    if index - offset >= 0
                    else index
                    - offset
                    + (abs(index - offset) // len(alphabet) + 1) * len(alphabet)
                )
            ]
            result = result + (
                new_letter.upper()
                if character.isupper() and derived_from_default_alphabet
                else new_letter
            )

        else:
            result = result + character

    return result
