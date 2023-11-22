# Author: Andrew Kim
# Version: 1.0.1
# Since: 4 November 2023
# Finds who paid their MySchoolBucks dues


# import external libraries
from os import listdir
from os.path import isfile, join
import base64


# filepath
FILEPATH = "C:\\Users\\Andrew\\Downloads\\dues\\"


# obtain file names
onlyfiles = [f for f in listdir(FILEPATH) if isfile(join(FILEPATH, f))]


# processes email file
# filename: name of email file
# return: name of person who paid dues
def read_email(filename: str) -> str:
    # open file
    f = open(FILEPATH + filename)
    base = f.read()

    # trim text
    base = base[base.index("Content-Transfer-Encoding: base64") : base.index("text/html")]
    base = base[:base.index("--")]
    base = base.replace("Content-Transfer-Encoding: base64", "").replace("\n", "")
    
    # decode from base64 to text
    text = str(base64.b64decode(base))

    # trim trimmed text
    if "Science Olympiad Dues" in text:
        text = text[text.index("Science Olympiad Dues") :]
        text = text.replace("Science Olympiad Dues", "")
        print(text)
        text = text[: text.index("\\r\\n\\r\\n")]
        name = text[: text.index("(")].replace(" ", "")
        tshirt = text[text.index(": ") :]
        text = name + tshirt
    else:
        text = text[text.index("Science Olympiad Donation") :]
        text = text.replace("Science Olympiad Donation", "")
        text = text[: text.index("(")].replace(" ", "").replace(",", ", ")

    # trim trimmed trimmed text

    # return and continue writing excellent comments
    return text


people = [read_email(filename) for filename in onlyfiles]
sorted_people = sorted(people)
print("\n".join(sorted_people))