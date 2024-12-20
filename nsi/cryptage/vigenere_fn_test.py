from vigenere_fn import code_vigenere, decode_vigenere
from constants import ALPHABET, SPECIAL_CHARACTERS


def test_code_vigenere_f_to_p():
    assert code_vigenere(text="f", alphabet=ALPHABET, keyword="keyword") == "p"


def test_code_vigenere_x_to_e():
    assert code_vigenere(text="x", alphabet=ALPHABET, keyword="hello") == "e"


def test_code_vigenere_message():
    assert (
        code_vigenere(text="Hello world", alphabet=ALPHABET, keyword="vigenere")
        == "Cmrpb nsmtj"
    )


def test_code_vigenere_special_characters():
    assert (
        code_vigenere(text=SPECIAL_CHARACTERS, alphabet=ALPHABET, keyword="word")
        == SPECIAL_CHARACTERS
    )


def test_decode_vigenere_z_to_d():
    assert decode_vigenere(text="z", alphabet=ALPHABET, keyword="world") == "d"


def test_decode_vigenere_b_to_z():
    assert decode_vigenere(text="b", alphabet=ALPHABET, keyword="cesar") == "z"


def test_decode_vigenere_message():
    assert (
        decode_vigenere(text="Cmrpb nsmtj", alphabet=ALPHABET, keyword="vigenere")
        == "Hello world"
    )


def test_decode_vigenere_special_characters():
    assert (
        decode_vigenere(text=SPECIAL_CHARACTERS, alphabet=ALPHABET, keyword="decode")
        == SPECIAL_CHARACTERS
    )
