"""Implement a function that returns True if text is an american phone number: a DDD-DDD-DDDD formated string.
"""


def is_phone_number_without_regex(text):
    if len(text) != 12:
        return False

    for i in range(12):
        if i in {3, 7} and text[i] != "-":
            return False
        if i not in {3, 7} and not text[i].isdigit():
            return False

    return True


if __name__ == '__main__':
    pass
