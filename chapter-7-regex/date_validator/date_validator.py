"""Implement a function thats validate a 'DD/MM/YYYY' formated string as a valid date.
"""

import re


DATE_PATTERN = re.compile(r'''
    (0[1-9]|[1-2]\d|3[0-1])  # a number between 01 and 31
    /
    (0[1-9]|1[0-2])  # a number between 01 and 12
    /
    (\d{4})  # a 4 digits number
''', re.VERBOSE)

DAYS_IN_MONTHS = [
    0,
    31, 29, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31,
]


def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    
    return False

def is_valid_date(text):
    """Check if a text is a 'DD/MM/YYYY' formated date and is a valid date.
    """
    if not is_valid_date_format(text):
        return False

    day, month, year = [int(n) for n in text.split('/')]

    if not (0 < day <= DAYS_IN_MONTHS[month]):
        return False

    if day == 29 and month == 2 and not is_leap_year(year):
        return False

    return True
    

def is_valid_date_format(text):
    """Check if a string as a 'DD/MM/YYYY' format.
    """
    return bool(re.search(DATE_PATTERN, text))


if __name__ == '__main__':
    pass
