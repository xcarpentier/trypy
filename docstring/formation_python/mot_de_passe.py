LETTERS = [
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
    "z",
]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def contains_letter(password: str) -> bool:
    contains_letter = False
    for letter in LETTERS:
        if letter in password:
            contains_letter = True
            break
        else:
            continue
    if contains_letter:
        return True
    else:
        return False


def contains_number(password: str) -> bool:
    contains_number = False
    for number in NUMBERS:
        if number in password:
            contains_number = True
            break
        else:
            continue
    if contains_number:
        return True
    else:
        return False


def contains_letter_and_number(password: str) -> bool:
    if contains_letter(password=password) and contains_number(password=password):
        return True
    else:
        return False


while True:
    password = input(
        "Enter your new password with at least 8 characters and with letters and numbers : "
    )
    if not password:
        print("You did not enter any password.")
    elif len(password) < 8:
        print("That password was too short.")
    elif not contains_letter_and_number(password=password):
        print(
            "That password had 8 characters or more but it contained letters only or numbers only."
        )
    elif contains_letter_and_number:
        print("Password accepted.")
        break
