# Author: Andrew Kim
# Version: 3.0.0
# Since: 27 November 2023
# Hill Cipher Encryption
# NOTE fix 3x3 encryption


# import local libraries
import tools
import quotes


# import external librarires
import random
import numpy as np
from itertools import chain



# values coprime with 26 for Hill Cipher
COPRIME_26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]



# 2x2 hill cipher
def hill(i: int = 1, plain: str = None, auth: str = None, k: str = None, decryption: bool = True):
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

    # generate key if key not already given
    key = hill_key()
    if k is not None:
        key = [tools.ALPHABET.index(letter) for letter in k]
    key_text = "".join([tools.ALPHABET[k] for k in key])

    # person is encoding plaintext
    if not decryption:
        print(f"Encode this Hill Cipher by {author} with the encryption key {key_text}")
        print(" ".join([letter for letter in plaintext]))
        return

    # adjust size of plaintext
    plaintext += "Z" if len(plaintext) % 2 == 1 else ""
    
    # get pairs of numbers
    pairings = [(tools.ALPHABET.index(plaintext[j]), tools.ALPHABET.index(plaintext[j + 1])) for j in range(0, len(plaintext) - 1, 2)]

    # multiply numbers
    cipher_numbers = []
    for pairing in pairings:
        cipher_numbers.append(key[0] * pairing[0] + key[1] * pairing[1])
        cipher_numbers.append(key[2] * pairing[0] + key[3] * pairing[1])

    # print question
    print(f"Decode this Hill Cipher by {author} with the encryption key {key_text}")
    print("".join([tools.ALPHABET[number % 26] for number in cipher_numbers]) + "\n")

    hill(i - 1, decryption=bool)



# create invertible hill cipher key
def hill_key() -> list:
    rand_key = lambda : [random.randint(0, 25) for i in range(4)]
    key = rand_key()
    while (key[0] * key[3]) - (key[1] * key[2]) not in COPRIME_26:
        key = rand_key()
    return key
   


# 3x3 hill cipher
def hill_3(i: int = 1, plain: str = None, auth: str = None, k: list = None):
    if i == 0:
        return
    
    plaintext, author = None, None

    if plain is None and auth is None and k is None:
        plaintext, author = quotes.random_quote(30)
        plaintext = tools.get_letters(plaintext)
    else:
        plaintext = tools.get_letters(plain)
        author = auth

    # adjust size of plaintext
    remainder = len(plaintext) % 3
    if remainder != 0:
        plaintext += ["X" for i in range(3 - remainder)]

    # get triplets of numbers - full 3x3 numerial matrices
    triplets = []
    for j in range(0, len(plaintext) - 1, 3):
        triplets.append([tools.ALPHABET.index(plaintext[j]), tools.ALPHABET.index(plaintext[j + 1]), tools.ALPHABET.index(plaintext[j + 2])])

    # get key
    # key, determinant = hill_3_key()
    key = [
        [0, 11, 15],
        [7, 0, 1],
        [4, 19, 0]
    ]
    determinant = round(np.linalg.det(key)) % 26
    print(key)
    adjoint = np.mod(np.linalg.inv(key) * determinant, 26)
    decryption_key = COPRIME_26[- COPRIME_26.index(determinant)] * adjoint
    
    # flatten decryption key
    decryption_numbers = np.mod(list(chain.from_iterable(decryption_key)), 26)
    print(decryption_numbers)

    # encrypt plaintext
    encrypted_triplets = []
    for triplet in triplets:
        encrypted_triplets.append(np.dot(key, triplet))
    
    # flatten encrypted numbers
    cipher_numbers = list(chain.from_iterable(encrypted_triplets))


    # print question
    print(f"Decode this Hill Cipher by {author} with the decryption key {''.join([tools.ALPHABET[int(number)] for number in decryption_numbers])}")
    print("".join([tools.ALPHABET[number % 26] for number in cipher_numbers]) + "\n")
    
    hill_3(i - 1)


# generates decryptible hill 3x3 key
def hill_3_key():
    rand_key = lambda : [[random.randint(0, 25) for i in range(3)] for j in range(3)]
    key = rand_key()
    determinant = 0
    while determinant not in COPRIME_26:
        key = rand_key()
        determinant = np.linalg.det(key)
    return key, determinant

