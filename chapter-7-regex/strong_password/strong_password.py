"""Implement a function that checks if a password is strong enough:
- at least 8 characters long
- contains both lowercase and upper case
- at leat one digit
"""

import re


DIGIT_PATTERN = re.compile(r'.*\d.*')
LENGTH_PATTERN = re.compile(r'.{8,}')
LOWERCASE_PATTERN = re.compile(r'.*[a-z].*')
UPPERCASE_PATTERN = re.compile(r'.*[A-Z].*')


def is_long_password(pwd):
    return bool(re.search(LENGTH_PATTERN, pwd))

def contains_digit(pwd):
    return bool(re.search(DIGIT_PATTERN, pwd))

def contains_lowercase(pwd):
    return bool(re.search(LOWERCASE_PATTERN, pwd))

def contains_uppercase(pwd):
    return bool(re.search(UPPERCASE_PATTERN, pwd))

def is_strong_password(pwd):
    return all(
        [
            is_long_password(pwd),
            contains_digit(pwd),
            contains_lowercase(pwd),
            contains_uppercase(pwd),
        ]
    )


if __name__ == '__main__':
    pass