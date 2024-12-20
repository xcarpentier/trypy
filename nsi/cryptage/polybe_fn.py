from typing import List
from code_fn import is_derived_from_default_alphabet


def generate_polybe_key(alphabet: List[str]):
    key = []

    for y in range(len(alphabet) // 5 + 1):
        new_row = []
        characters = alphabet[y * 5 : (y + 1) * 5]
        for character in characters:
            new_row.append(character)

        key.append(new_row)

    return key


def code_polybe(alphabet: List[str], text: str):
    """Return the message coded with Polybe key.

    text : str

    return : str"""

    key = generate_polybe_key(alphabet=alphabet)
    derived_from_default_alphabet = is_derived_from_default_alphabet(alphabet=alphabet)
    result = ""

    for character in text:
        if (
            character.lower() if derived_from_default_alphabet else character
        ) in alphabet:
            for row in key:
                if (
                    character.lower() if derived_from_default_alphabet else character
                ) in row:
                    result = result + (
                        str(key.index(row))
                        + str(
                            row.index(
                                character.lower()
                                if derived_from_default_alphabet
                                else character
                            )
                        )
                    )

        else:
            result = result + character

    return result


def decode_polybe(alphabet: List[str], text: str):
    """Return the message decoded with Polybe key.

    text : str

    return : str"""

    key = generate_polybe_key(alphabet=alphabet)
    result = ""

    index = 0
    while index < len(text):
        if (
            text[index].isdigit()
            and int(text[index]) < len(key)
            and index + 1 < len(text)
            and text[index + 1].isdigit()
            and int(text[index + 1]) < len(key[0])
        ):
            result = result + key[int(text[index])][int(text[index + 1])]
            index += 2

        else:
            result = result + text[index]
            index += 1

    return result
