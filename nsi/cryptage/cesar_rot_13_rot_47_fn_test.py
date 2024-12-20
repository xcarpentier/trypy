from constants import ALPHABET, ASCII_ALPHABET, SPECIAL_CHARACTERS
from cesar_rot_13_rot_47_fn import code_cesar_rot_13_rot_47, decode_cesar


def test_code_rot_13_a_to_n():
    assert code_cesar_rot_13_rot_47(text="a", alphabet=ALPHABET, offset=13) == "n"


def test_code_rot_13_n_to_a():
    assert code_cesar_rot_13_rot_47(text="n", alphabet=ALPHABET, offset=13) == "a"


def test_code_rot_13_message():
    assert (
        code_cesar_rot_13_rot_47(text="Hello world", alphabet=ALPHABET, offset=13)
        == "Uryyb jbeyq"
    )


def test_decode_rot_13_message():
    assert (
        code_cesar_rot_13_rot_47(text="Uryyb jbeyq", alphabet=ALPHABET, offset=13)
        == "Hello world"
    )


def test_reverse_rot_13():
    assert (
        code_cesar_rot_13_rot_47(
            text=code_cesar_rot_13_rot_47(
                text="Hello world", alphabet=ALPHABET, offset=13
            ),
            alphabet=ALPHABET,
            offset=13,
        )
        == "Hello world"
    )


def test_rot_13_special_characters():
    assert (
        code_cesar_rot_13_rot_47(text=SPECIAL_CHARACTERS, alphabet=ALPHABET, offset=13)
        == SPECIAL_CHARACTERS
    )


def test_code_rot_47_paranthesis_to_W():
    assert code_cesar_rot_13_rot_47(text="(", alphabet=ASCII_ALPHABET, offset=47) == "W"


def test_code_rot_47_W_to_parathesis():
    assert code_cesar_rot_13_rot_47(text="W", alphabet=ASCII_ALPHABET, offset=47) == "("


def test_code_rot_47_message():
    assert (
        code_cesar_rot_13_rot_47(text="Hello world", alphabet=ASCII_ALPHABET, offset=47)
        == "w6==@ H@C=5"
    )


def test_decode_rot_47_message():
    assert (
        code_cesar_rot_13_rot_47(text="w6==@ H@C=5", alphabet=ASCII_ALPHABET, offset=47)
        == "Hello world"
    )


def test_reverse_rot_47():
    assert code_cesar_rot_13_rot_47(
        text=code_cesar_rot_13_rot_47(
            text="Hello world !!!", alphabet=ASCII_ALPHABET, offset=47
        ),
        alphabet=ASCII_ALPHABET,
        offset=47,
    )


def test_code_cesar_a_to_d():
    assert code_cesar_rot_13_rot_47(text="a", alphabet=ALPHABET, offset=3) == "d"


def test_code_cesar_u_to_e():
    assert code_cesar_rot_13_rot_47(text="u", alphabet=ALPHABET, offset=10) == "e"


def test_code_cesar_message():
    assert (
        code_cesar_rot_13_rot_47(text="Hello world", alphabet=ALPHABET, offset=5)
        == "Mjqqt btwqi"
    )


def test_code_cesar_special_characters():
    assert (
        code_cesar_rot_13_rot_47(text=SPECIAL_CHARACTERS, alphabet=ALPHABET, offset=12)
        == SPECIAL_CHARACTERS
    )


def test_decode_cesar_d_to_b():
    assert decode_cesar(text="d", alphabet=ALPHABET, offset=2) == "b"


def test_decode_cesar_a_to_z():
    assert decode_cesar(text="a", alphabet=ALPHABET, offset=1) == "z"


def test_decode_cesar_message():
    assert (
        decode_cesar(text="Spwwz hzcwo", alphabet=ALPHABET, offset=11) == "Hello world"
    )


def test_decode_cesar_special_characters():
    assert (
        decode_cesar(
            text=SPECIAL_CHARACTERS,
            alphabet=ALPHABET,
            offset=1,
        )
        == SPECIAL_CHARACTERS
    )
