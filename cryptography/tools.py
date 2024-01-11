# Author: Andrew Kim
# Version: 3.1.0
# Since: 25 October 2023
# String manipulation tools


# alphabet
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# punctuation characters
PUNCTUATION = '''!()-[]{};:'"\,,<>./?@#$%^&*_~'''



# turns letters into list of numbers
def to_numbers(plain: str) -> list:
    return [ALPHABET.index(letter) for letter in plain]


# removes all puncutation and spaces (leaves only letters)
def get_letters(plain: str) -> list:
    return [letter for letter in list(plain.upper()) if letter in ALPHABET]


# removes punctuation
def remove_punctuation(plain: str, strip: bool = True) -> str:
    cleaned = plain
    for punc in PUNCTUATION:
        cleaned = cleaned.replace(punc, "")
    plain = plain.replace("  ", " ")
    return cleaned
