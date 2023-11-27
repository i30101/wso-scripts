# Author: Andrew Kim
# Version: 3.0.0
# Since: 25 November 2023
# Fractionated Morse Cipher Encryption


# import local libraries
import tools
import quotes


# morse chart
MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--.."
}

# fractionated chart
FRACTIONATED = list({
    "A": "...", "B": "..-", "C": "..x", "D": ".-.", "E": ".--", "F": ".-x", "G": ".x.",
    "H": ".x-", "I": ".xx", "J": "-..", "K": "-.-", "L": "-.x", "M": "--.", "N": "---",
    "O": "--x", "P": "-x.", "Q": "-x-", "R": "-xx", "S": "x..", "T": "x.-", "U": "x.x",
    "V": "x-.", "W": "x--", "x": "x-x", "Y": "xx.", "Z": "xx-"
}.values())



# translates text to morse
def to_morse(plain: str) -> str:
    plaintext = tools.remove_punctuation(plain).upper()
    morse_text = ""
    for i, char in enumerate(plaintext):
        if char != " ":
            morse_text += MORSE[char]
        if i != len(plaintext) - 1:
            morse_text += "x"
    morse_text = morse_text.replace("xxx", "")
    return morse_text



# fractionated morse cipher
def fractionated(i: int = 1, plain: str = None, auth: str = None):
    if i == 0:
        return
    
    plaintext = plain
    morse_text = None
    author = None

    # cipher and author not given
    if plain is None and auth is None:
        plaintext, author = quotes.random_quote()
        morse_text = to_morse(plaintext)
    # quote info given
    else:
        morse_text = to_morse(plain)
        author = auth
    
    # adjust length for transcription
    if int(len(morse_text)) % 3 != 0:
        morse_text += "".join(["x" for i in range(3 - (len(morse_text) % 3))])

    # get random word
    rand = quotes.random_word().upper()

    # ciphertext alphabet
    cipher_alphabet = rand + "".join([l for l in tools.ALPHABET if l not in rand])

    # encryption
    cipher_text = ""
    for j in range(0, len(morse_text), 3):
        triplet = morse_text[j: j + 3]
        letter = cipher_alphabet[FRACTIONATED.index(triplet)]
        cipher_text += letter

    # print question
    print(f"Solve this Fractionated Morse cipher by {author} that ends with the word{plaintext[plaintext.rindex(' '):].upper()}")
    print("  ".join(cipher_text) + "\n")
    
    fractionated(i - 1)


