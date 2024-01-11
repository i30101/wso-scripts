# Author: Andrew Kim
# Version: 3.1.0
# Since: 28 November 2023
# Nihilist Cipher Encryption


# import local libraries
import tools
import quotes


# finds polybius value for given coordinates
def polybius_num(l: str, table: list) -> int:
    row = 0
    col = 0
    for r in range(5):
        for c in range(5):
            if l in table[r][c]:
                row = r
                col = c
    return 10 * (row + 1) + col + 1


# encrypts plaintext using the Nihilist Cipher
def nihilist(i: int = 1, plain: str = None, auth: str = None, k: str = None, polyb: str = None):
    if i == 0:
        return
    
    plaintext, author = None, None

    # cipher and author not given
    if plain is None and auth is None:
        plaintext, author = quotes.random_quote()
        plaintext = tools.get_letters(plaintext)
    # quote info given
    else:
        plaintext = tools.get_letters(plain)
        author = auth

    # generate keywords
    keyword = quotes.random_word().upper() if k is None else k.upper()
    polyb_key = quotes.random_word().upper() if polyb is None else polyb.upper()

    # create polybius table
    i_index = tools.ALPHABET.index("I")
    split_alph = list(tools.ALPHABET[: i_index]) + ["IJ"] + list(tools.ALPHABET[i_index + 2 :])
    
    # check if I and J are both in the letter
    if "I" in polyb_key and "J" in polyb_key:
        raise Exception("Polybius key cannot be entered into grid.")
    
    polybius_alph = []
    for letter in polyb_key:
        if letter == "I" or letter == "J":
            polybius_alph.append("IJ")
        else:
            polybius_alph.append(letter)

    polybius_alph += [letter for letter in split_alph if letter not in polybius_alph]

    polybius = [list(range(5)) for j in range(5)]
    for j, letter in enumerate(polybius_alph):
        polybius[int(j / 5)][j % 5] = letter
    
    # encrypt cipher
    cipher_numbers = []
    for j, letter in enumerate(plaintext):
        cipher_numbers.append(str(polybius_num(keyword[j % len(keyword)], polybius) + polybius_num(letter, polybius)))
    print(f"Solve this Nihilist cipher by {author} with the keyword {keyword} and the Polybius key {polyb_key}.")
    print(" ".join(cipher_numbers) + "\n")
