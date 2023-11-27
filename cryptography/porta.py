# Author: Andrew Kim
# Version: 3.0.0
# Since: 27 November 2023
# Porta Cipher Encryption


# import local libraries
import tools
import quotes



# porta cipher
def porta(i: int = 1, plain: str = None, auth: str = None):
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

    # get keyword
    keyword = quotes.random_word(False).upper()
    
    # split alphabet
    first_half = tools.ALPHABET[:13]
    second_half = tools.ALPHABET[13:]
    
    rows = [second_half[i:] + second_half[:i] for i in range(13)]
    
    # encryption
    ciphertext = ""
    for j, plainLetter in enumerate(plaintext):
        row_index = int(tools.ALPHABET.index(keyword[j % len(keyword)]) / 2)
        if plainLetter in first_half:
            ciphertext += rows[row_index][first_half.index(plainLetter)]
        else:
            ciphertext += tools.ALPHABET[rows[row_index].index(plainLetter)]
    
    # print question
    print(f"Solve this Porta cipher by {author} with the keyword {keyword}.")
    print(ciphertext + "\n")
    
    porta(i - 1)
