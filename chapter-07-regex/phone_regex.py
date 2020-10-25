"""Implement a function that returns True if text is an american phone number: DDD-DDD-DDDD (only format accepted by is_vaid_phone_number_without_regex)
DDD DDD DDDD
(DDD)-DDD-DDDD
(DDD) DDD DDDD
"""

import re


def is_valid_phone_number_without_regex(text):
    if len(text) != 12:
        return False

    for i in range(12):
        if i in {3, 7} and text[i] != "-":
            return False
        if i not in {3, 7} and not text[i].isdigit():
            return False

    return True

def is_valid_phone_number_with_regex(text):
    pattern = r"\d{3}-\d{3}-\d{4}"
    pattern += r"|\d{3} \d{3} \d{4}"
    pattern += r"|\(?\d{3}\)?-\d{3}-\d{4}"
    pattern += r"|\(?\d{3}\)? \d{3} \d{4}"
    
    return bool(re.search(pattern, text))


if __name__ == '__main__':
    pass
