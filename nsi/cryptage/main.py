from constants import (
    ALPHABET,
    ASCII_ALPHABET,
    CUSTOM_ALPHABET,
)
from interface_fn import (
    get_option_choice,
    get_code_key,
    get_custom_alphabet,
    get_alphabet_choice,
    get_alphabet_with_keyword_choice,
    get_alphabet_keyword,
    get_cesar_offset,
    get_vigenere_keyword,
    get_message,
)
from cesar_rot_13_rot_47_fn import code_cesar_rot_13_rot_47, decode_cesar
from vigenere_fn import code_vigenere, decode_vigenere
from polybe_fn import code_polybe, decode_polybe
from code_fn import generate_alphabet_with_keyword


while True:
    option_choice = get_option_choice()

    if option_choice == "1" or option_choice == "2":
        code_key = get_code_key()

        if (
            code_key == "1"
            or code_key == "2"
            or code_key == "3"
            or code_key == "4"
            or code_key == "5"
        ):
            if code_key == "1":
                alphabet = ALPHABET

            elif code_key == "2":
                alphabet = ASCII_ALPHABET

            if code_key == "3" or code_key == "4" or code_key == "5":
                alphabet_choice = get_alphabet_choice()

                if alphabet_choice == "1":
                    alphabet = ALPHABET

                elif alphabet_choice == "2":
                    alphabet = ASCII_ALPHABET

                elif alphabet_choice == "3":
                    alphabet = CUSTOM_ALPHABET

                elif alphabet_choice == "":
                    continue

            alphabet_with_keyword_choice = get_alphabet_with_keyword_choice()

            if alphabet_with_keyword_choice == "o":
                alphabet_keyword = get_alphabet_keyword(alphabet=alphabet)

                if alphabet_keyword == "":
                    continue

                else:
                    alphabet = generate_alphabet_with_keyword(
                        alphabet=alphabet, keyword=alphabet_keyword
                    )

            elif alphabet_with_keyword_choice == "":
                continue

            if code_key == "3":
                offset = get_cesar_offset()

                if offset == "":
                    continue

            elif code_key == "4":
                keyword = get_vigenere_keyword(alphabet=alphabet)

                if keyword == "":
                    continue

            message = get_message()

            if message == "":
                continue

            if option_choice == "1":
                if code_key == "1":
                    response = code_cesar_rot_13_rot_47(
                        text=message, alphabet=alphabet, offset=13
                    )

                elif code_key == "2":
                    response = code_cesar_rot_13_rot_47(
                        text=message, alphabet=alphabet, offset=47
                    )

                elif code_key == "3":
                    response = code_cesar_rot_13_rot_47(
                        text=message, alphabet=alphabet, offset=int(offset)
                    )

                elif code_key == "4":
                    response = code_vigenere(
                        text=message, alphabet=alphabet, keyword=keyword
                    )

                elif code_key == "5":
                    response = code_polybe(text=message, alphabet=alphabet)

            elif option_choice == "2":
                if code_key == "1":
                    response = code_cesar_rot_13_rot_47(
                        text=message, alphabet=alphabet, offset=13
                    )

                elif code_key == "2":
                    response = code_cesar_rot_13_rot_47(
                        text=message, alphabet=alphabet, offset=47
                    )

                elif code_key == "3":
                    response = decode_cesar(
                        text=message, alphabet=alphabet, offset=int(offset)
                    )

                elif code_key == "4":
                    response = decode_vigenere(
                        text=message, alphabet=alphabet, keyword=keyword
                    )

                elif code_key == "5":
                    response = decode_polybe(text=message, alphabet=alphabet)

        elif code_key == "":
            continue

        print(
            f"""Voici votre message crypté ou décrypté :

{response}\n"""
        )

    elif option_choice == "3":
        get_custom_alphabet()

    elif option_choice == "":
        break
