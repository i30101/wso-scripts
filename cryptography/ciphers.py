# Author: Andrew Kim
# Version: 2.1.2
# Since: 25 October 2023
# Encryption and decryption


# import external libraries
import random


# import quot generator methods
from quotes import random_word
from quotes import random_quote


# morse chart
MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--.."
}

# alphabet
ALPHABET = list(MORSE.keys())

# fractionated chart
FRACTIONATED = list({
    "A": "...", "B": "..-", "C": "..x", "D": ".-.", "E": ".--", "F": ".-x", "G": ".x.",
    "H": ".x-", "I": ".xx", "J": "-..", "K": "-.-", "L": "-.x", "M": "--.", "N": "---",
    "O": "--x", "P": "-x.", "Q": "-x-", "R": "-xx", "S": "x..", "T": "x.-", "U": "x.x",
    "V": "x-.", "W": "x--", "x": "x-x", "Y": "xx.", "Z": "xx-"
}.values())

# values coprime with 26 for Hill Cipher
COPRIME_26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

# punctuation characters
PUNCTUATION = '''!()-[]{};:'"\,,<>./?@#$%^&*_~'''



# turns letters into list of numbers
def to_numbers(plain: str) -> list:
    return [ALPHABET.index(letter) for letter in plain]


# removes all puncutation and spaces (leaves only letters)
def get_letters(plain: str) -> str:
    return [letter for letter in plain.upper() if letter in ALPHABET]


# removes punctuation
def remove_punctuation(plain: str, strip: bool = True) -> str:
    cleaned = plain
    for punc in PUNCTUATION:
        cleaned = cleaned.replace(punc, "")
    return cleaned


# translates text to morse
def to_morse(plain: str) -> str:
    plaintext = remove_punctuation(plain).upper()
    morse_text = ""
    for i, char in enumerate(plaintext):
        if char == " ":
            morse_text += "xx"
        else:
            morse_text += MORSE[char]
            if i != len(plaintext) - 1:
                morse_text += "x"
    return morse_text



# fractionated morse cipher
def fractionated(plain: str, author: str):
    # translate plaintext to morse
    morse_text = to_morse(plain)

    # adjust length for transcription
    if int(len(morse_text)) % 3 != 0:
        morse_text += "".join(["x" for i in range(3 - (len(morse_text) % 3))])

    # get random word
    rand = random_word().upper()

    # ciphertext alphabet
    cipher_alphabet = rand + "".join([l for l in ALPHABET if l not in rand])

    # encryption
    cipher_text = ""
    for i in range(0, len(morse_text), 3):
        triplet = morse_text[i: i + 3]
        # print(triplet)
        letter = cipher_alphabet[FRACTIONATED.index(triplet)]
        cipher_text += letter

    # print question
    print(f"Solve this Fractionated Morse cipher by {author} that ends with the word {plain[plain.rindex(' '):].upper()}\n")
    print("  ".join(cipher_text))



# complete columnar transposition cipehr
def columnar():
    new_quote = random_quote()
    quote = ""
    author = ""
    num_columns = 0

    # find a complete quote
    griddable = False
    while not griddable:
        new_quote = random_quote()
        quote = get_letters(new_quote["quote"])
        author = new_quote["author"]

        available_columns = list(range(4, 10))

        for i in range(len(available_columns)):
            rand_column = random.choice(available_columns)
            if len(quote) % rand_column == 0:
                num_columns = rand_column
                griddable = True
                break
            available_columns.remove(rand_column)

    # put letters in columns
    columns = ["" for i in range(num_columns)]
    for i in range(len(quote)):
        columns[i % num_columns] += quote[i]

    # shuffle columns
    random.shuffle(columns)

    print(f"Solve this Complete Columnar Transposition cipher by {author}.")
    print("".join(columns))



# incompelte columnar transposition cipher
# some columns are incomplete, imperfect grid of letters
def columnar_key(plain: str, author: str):
    plaintext = get_letters(plain)
    # print(plaintext)

    # get keyword
    keyword = random_word(False).upper()
    num_letters = len(keyword)

    # put letters into columns
    columns = [[] for i in range(num_letters)]

    # store column for each letter
    for i, letter in enumerate(plaintext):
        columns[i % num_letters].append(letter)

    # lists for adding columns to ciphertext in order :clown:
    num_list = [ALPHABET.index(letter) for letter in keyword]
    index_list = list(range(num_letters))
    key_list = list(keyword)

    ciphertext = ""

    # add each column to ciphertext in proper order
    # NOTE do not use i to reference any avlues in lists
    for i in range(num_letters):
        lowest_letter_num = min(num_list)
        lowest_letter_index = index_list[num_list.index(lowest_letter_num)]

        ciphertext += "".join(columns[lowest_letter_index])

        num_list.remove(lowest_letter_num)
        index_list.remove(lowest_letter_index)

    print(f"Solve this Complete Columnar Transposition cipher by {author} with the keyword {keyword}.")
    print(ciphertext)



# porta cipher
def porta(plain: str, author: str):
    plaintext = get_letters(plain)

    # get keyword
    keyword = random_word(False).upper()
    
    # split alphabet
    first_half = ALPHABET[:13]
    second_half = ALPHABET[13:]
    
    rows = [second_half[i:] + second_half[:i] for i in range(13)]
    
    # encryption
    ciphertext = ""
    for i, plainLetter in enumerate(plaintext):
        row_index = int(ALPHABET.index(keyword[i % len(keyword)]) / 2)
        if plainLetter in first_half:
            ciphertext += rows[row_index][first_half.index(plainLetter)]
        else:
            ciphertext += ALPHABET[rows[row_index].index(plainLetter)]
    
    # print question
    print(f"Solve this Porta cipher by {author} with the keyword {keyword}.")
    print(ciphertext)



# create invertible hill cipher key
def hill_key() -> list:
    rand_digits = lambda : [random.randint(0, 25) for i in range(4)]
    key = rand_digits()
    while not is_invertible(key):
        key = rand_digits()
    return key



# whether key is invertible or not
def is_invertible(key: list) -> bool:
    return (key[0] * key[3]) - (key[1] * key[2]) in COPRIME_26



# 2x2 hill cipher
def hill(plain: str, author: str, k: str = None, decryption: bool = True):
    plaintext = get_letters(plain)

    # generate key if key not already given
    key = hill_key()
    if k is not None:
        key = [ALPHABET.index(letter) for letter in k]
    key_text = "".join([ALPHABET[k] for k in key])

    # person is encoding plaintext
    if not decryption:
        print(f"Encode this Hill Cipher by {author} with the encryption key {key_text}")
        print(" ".join([letter for letter in plaintext]))
        return

    # adjust size of plaintext
    plaintext += "Z" if len(plaintext) % 2 == 1 else ""
    
    # get pairs of numbers
    pairings = [(ALPHABET.index(plaintext[i]), ALPHABET.index(plaintext[i + 1])) for i in range(0, len(plaintext) - 1, 2)]

    # multiply numbers
    cipher_numbers = []
    for pairing in pairings:
        cipher_numbers.append(key[0] * pairing[0] + key[1] * pairing[1])
        cipher_numbers.append(key[2] * pairing[0] + key[3] * pairing[1])

    # print question
    print(f"Decode this Hill Cipher by {author} with the encryption key {key_text}")
    print("".join([ALPHABET[number % 26] for number in cipher_numbers]))
   


# 3x3 hill cipher
def hill3(plain: str, author: str):
    pass



# nihilist cipher
def nihilist(plain: str, author: str):
    pass




if __name__ == "__main__":
    for i in range(16):
        quote = random_quote()
        fractionated(quote["quote"], quote["author"])
