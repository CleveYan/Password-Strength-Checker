import re

"""
Requirements: Input, Validation, Output

Input: Enter Password

Validation: Check the length, complexity(uppercase, lowercase, numbers, symbols),
compare with common passwords

Output: weak, medium, strong | 5-star rating based within 8-20 length | api for how long to crack?

Ratings guidelines: 10 Categories, Length 0,1,2,3, 4 ; UpperCase: 0,1,2 ; LowerCase: 0,1,2 ; Numbers: 0,1,2 ; Symbols ;
Compare rating to Guidelines.
"""

weak = "weak"
medium = "medium"
strong = "strong"
vstrong = "very strong"
count = 0


# password
def get_password():
    password = ''
    while password == '' :
        password = str(input("Enter your password: "))
    else:
        return password


# check length
def check_length(pw):
    if len(pw) < 8:
        return count
    elif 7 < len(pw) < 13:
        return count + 2
    if 12 < len(pw) < 26:
        return count + 3
    if len(pw) > 25:
        return count + 4


def check_upper(pw):
    if re.search(r"[A-Z]", pw) is None:
        return count + 0
    else:
        return count + 1


def check_lower(pw):
    if re.search(r"[a-z]", pw) is None:
        return count + 0
    else:
        return count + 1


def check_num(pw):
    if re.search(r"\d", pw) is None:
        return count + 0
    else:
        return count + 1


def check_symbols(pw):
    if re.search(r"\W", pw) is None:
        return count + 0
    else:
        return count + 1


def tally(counter):
    if counter < 4:
        return weak
    elif 4 <= counter < 6:
        return  medium
    elif 6 <= counter < 8:
        return strong
    else:
        return vstrong
