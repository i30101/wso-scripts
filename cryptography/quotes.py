# Author: Andrew Kim
# Version: 2.0.1
# Since: 25 October 2023
# Quote generation tools


# import external libraries
import requests
import ast


# read API key
lines = None
with open("./cryptography/key.txt") as file:
    lines = file.readlines()

KEY = lines[0].strip()
URL = lines[1].strip()



# check if word is isogram
def is_isogram(word: str) -> bool:
    return [word.count(letter) for letter in word] == [1 for n in word]


# get random word 
def random_word(isogram: bool = True, min: int = 4, max: int = 8) -> str:
    word_api = URL + "randomword"
    while True:
        # get word from API
        response = requests.get(word_api, headers={"X-Api-Key": KEY})
        if response.status_code == requests.codes.ok:
            # format raw text
            response = response.text.replace("{\"word\": \"", "").replace("\"}", "")

            # word is proper length
            if min <= len(response) <= max:
                # isogram not desired or isogram desired and word is isogram
                if not isogram or is_isogram(response):
                    return response


# get random quote
def random_quote():
    quote_api = URL + "quotes"
    while True:
        response = requests.get(quote_api, headers={'X-Api-Key': KEY})
        if response.status_code == requests.codes.ok:
            quote_dict = ast.literal_eval(response.text.replace("[", "").replace("]", ""))
            quote = quote_dict["quote"]
            if (
                quote.count(".") < 2 and    # less than two sentences
                quote.count(",") < 4 and    # less than four commas
                len(quote) < 100 and        # less than 100 characters
                not any(char.isdigit() for char in quote)   # quote does not have numbers

            ):
                return quote_dict
        else:
            print("Error: ", response.status_code, response.text)
