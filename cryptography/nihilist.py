# Author: Andrew Kim
# Version: 3.1.0
# Since: 28 November 2023
# Nihilist Cipher Encryption


# import local libraries
import tools
import quotes


# import external libraries
import random


# letters that can be removed from polybius table
remove_letters = "JVWKQZ"


# finds polybius value for given coordinates
def polybius_num(l: str, table: list) -> int:
    row = 0
    col = 0
    for r in range(5):
        for c in range(5):
            if table[r][c] == l:
                row = r
                col = c
    return 10 * (row + 1) + col + 1


# finds polybius letter for given numbers
def polybius_letters(n: int, table: list) -> str:
    row = int(n / 5) - 1
    col = n % 5
    return table[row][col]


# encrypts plaintext using Nihilist Cipher
def nihilist(i: int = 1, plain: str = None, auth: str = None, k: str = None):
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
    keyword = quotes.random_word().upper()
    polybius_letters = quotes.random_word().upper()

    # turn polybius key into isogram
    polybius_key = "".join([char for j, char in enumerate(polybius_letters) if char not in polybius_letters[:j]])

    # pick letter to be removed from polybius table
    removables = list(remove_letters)
    removed_letter = random.choice(removables)
    while remove_letters in plaintext and polybius_key:
        removables.remove(removed_letter)
        removed_letter = random.choice(removables)

    # create polybius table
    polybius_alph = polybius_key + "".join([letter for letter in tools.ALPHABET if letter != removed_letter and letter not in polybius_key])
    print(f"length of polybius alphabet: {len(polybius_alph)}")
    if len(polybius_alph) > 25:
        print(polybius_alph)
    polybius = [list(range(5)) for j in range(5)]
    for j, letter in enumerate(polybius_alph):
        polybius[int(j / 5)][j % 5] = letter
    
    cipher_numbers = []
    for j, letter in enumerate(plaintext):
        cipher_numbers.append(str(polybius_num(keyword[j % len(keyword)], polybius) + polybius_num(letter, polybius)))

    # print question
    print(f"Solve this Nihilist cipher by {author} with the keyword {keyword} and the Polybius keyword {polybius_letters}.")
    print(" ".join(cipher_numbers) + "\n")

    nihilist(i - 1)