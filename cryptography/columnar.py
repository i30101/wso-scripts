# Author: Andrew Kim
# Version: 3.1.0
# Since: 27 November 2023
# Columnar Cipher encryption


# import local libraries
import tools
import quotes


# import external libraries
import random


# complete columnar transposition cipher
def columnar(i: int = 1):
    if i == 0:
        return

    quote, author = quotes.random_quote()
    num_columns = 0

    # find a complete quote
    griddable = False
    while not griddable:
        quote, author = quotes.random_quote()
        quote = tools.get_letters(quote)

        available_columns = list(range(4, 10))

        for j in range(len(available_columns)):
            rand_column = random.choice(available_columns)
            if len(quote) % rand_column == 0:
                num_columns = rand_column
                griddable = True
                break
            available_columns.remove(rand_column)

    # put letters in columns
    columns = ["" for i in range(num_columns)]
    for j in range(len(quote)):
        columns[j % num_columns] += quote[j]

    # shuffle columns
    random.shuffle(columns)

    print(f"Solve this Complete Columnar Transposition cipher by {author}.")
    print("".join(columns) + "\n")

    columnar(i - 1)


# new columnar transposition cipher
def new_columnar():
    quote, author = quotes.random_quote()
    quote = tools.remove_punctuation(quote).upper()
    
    words = quote.split(" ")
    crib = random.choice([word for word in words if len(word) > 5])

    print(words)
    print(crib)

    # choose number of columns
    max_columns = 9 if len(crib) > 8 else len(crib) + 1
    num_columns = random.randint(4, max_columns)

    # adjust ciphertext 
    quote = tools.get_letters(quote)
    remainder = len(quote) % num_columns
    if remainder != 0:
        quote += "X" * (num_columns - remainder)

    print(quote)

    # put letters in columns
    columns = ["" for i in range(num_columns)]
    for j in range(len(quote)):
        columns[j % num_columns] += quote[j]

    # shuffle columns
    random.shuffle(columns)

    




# incompelte columnar transposition cipher
# some columns are incomplete, imperfect grid of letters
def columnar_key(i: int = 1, plain: str = None, auth: str = None):
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
    num_letters = len(keyword)

    # put letters into columns
    columns = [[] for i in range(num_letters)]

    # store column for each letter
    for j, letter in enumerate(plaintext):
        columns[j % num_letters].append(letter)

    # lists for adding columns to ciphertext in order :clown:
    num_list = [tools.ALPHABET.index(letter) for letter in keyword]
    index_list = list(range(num_letters))
    key_list = list(keyword)

    ciphertext = ""

    # add each column to ciphertext in proper order
    # NOTE do not use i to reference any avlues in lists
    for j in range(num_letters):
        lowest_letter_num = min(num_list)
        lowest_letter_index = index_list[num_list.index(lowest_letter_num)]

        ciphertext += "".join(columns[lowest_letter_index])

        num_list.remove(lowest_letter_num)
        index_list.remove(lowest_letter_index)

    print(f"Solve this Complete Columnar Transposition cipher by {author} with the keyword {keyword}.")
    print(ciphertext + "\n")
    columnar_key(i - 1)


new_columnar()