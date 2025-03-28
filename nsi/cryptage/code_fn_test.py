from code_fn import generate_alphabet_with_keyword, is_derived_from_default_alphabet
from constants import ALPHABET, ASCII_ALPHABET


def test_generate_alphabet_with_keyword_default_alphabet():
    assert generate_alphabet_with_keyword(alphabet=ALPHABET, keyword="default") == [
        "d",
        "e",
        "f",
        "a",
        "u",
        "l",
        "t",
        "b",
        "c",
        "g",
        "h",
        "i",
        "j",
        "k",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]


def test_generate_alphabet_with_keyword_ascii_alphabet():
    assert generate_alphabet_with_keyword(
        alphabet=ASCII_ALPHABET, keyword="(=$_z}8~!"
    ) == [
        "(",
        "=",
        "$",
        "_",
        "z",
        "}",
        "8",
        "~",
        "!",
        '"',
        "#",
        "%",
        "&",
        "'",
        ")",
        "*",
        "+",
        ",",
        "-",
        ".",
        "/",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "9",
        ":",
        ";",
        "<",
        ">",
        "?",
        "@",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "[",
        "\\",
        "]",
        "^",
        "`",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "{",
        "|",
    ]


def test_generate_with_keyword_custom_alphabet():
    assert generate_alphabet_with_keyword(
        alphabet=[
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            "q",
            "w",
            "e",
            "r",
            "t",
            "y",
            "u",
            "i",
            "o",
            "p",
            "a",
            "s",
            "d",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            "z",
            "x",
            "c",
            "v",
            "b",
            "n",
            "m",
        ],
        keyword="6yrt3bs0",
    ) == [
        "6",
        "y",
        "r",
        "t",
        "3",
        "b",
        "s",
        "0",
        "1",
        "2",
        "4",
        "5",
        "7",
        "8",
        "9",
        "q",
        "w",
        "e",
        "u",
        "i",
        "o",
        "p",
        "a",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "z",
        "x",
        "c",
        "v",
        "n",
        "m",
    ]


def test_is_derived_from_default_alphabet():
    assert is_derived_from_default_alphabet(
        alphabet=[
            "m",
            "t",
            "c",
            "h",
            "s",
            "g",
            "a",
            "b",
            "d",
            "e",
            "f",
            "i",
            "j",
            "k",
            "l",
            "n",
            "o",
            "p",
            "q",
            "r",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
    )


def test_is_not_derived_from_default_alphabet():
    assert not is_derived_from_default_alphabet(
        alphabet=[
            "m",
            "t",
            "c",
            "h",
            "s",
            "g",
            "a",
            "b",
            "d",
            "4",
            "e",
            "f",
            "i",
            "j",
            "k",
            "l",
            "n",
            "o",
            "p",
            "-",
            "%",
            "1",
            "q",
            "r",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
    )
