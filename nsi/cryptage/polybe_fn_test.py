from polybe_fn import code_polybe, decode_polybe
from constants import ALPHABET, SPECIAL_CHARACTERS


def test_code_polybe_a_to_00():
    assert code_polybe(text="a", alphabet=ALPHABET) == "00"


def test_code_polybe_message():
    assert code_polybe(text="Hello world", alphabet=ALPHABET) == "1204212124 4224322103"


def test_code_polybe_special_characters():
    assert code_polybe(text=SPECIAL_CHARACTERS, alphabet=ALPHABET) == SPECIAL_CHARACTERS


def test_decode_polybe_00_to_a():
    assert decode_polybe(text="00", alphabet=ALPHABET) == "a"


def test_decode_polybe_message():
    assert (
        decode_polybe(text="1204212124 4224322103", alphabet=ALPHABET) == "hello world"
    )


def test_decode_polybe_too_big_numbers():
    assert decode_polybe(text="1806729486", alphabet=ALPHABET) == "1806729486"


def test_decode_polybe_special_characters():
    assert (
        decode_polybe(text=SPECIAL_CHARACTERS, alphabet=ALPHABET) == SPECIAL_CHARACTERS
    )
