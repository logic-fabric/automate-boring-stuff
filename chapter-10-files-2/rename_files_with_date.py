"""Implement a function that rename files containing an american MM-DD-YYYY date to the same name with a european DD-MM-YYY.
"""

import os
import re
import shutil


AMERICAN_DATE_PATTERN = re.compile(r"""
    (0[1-9]|1[0-2])  # MM is an integer between 1 and 12
    -
    (O[1-9]|[12]\d|3[01])  # DD is an integer between 1 and 31
    -
    ([12]\d\d\d)  # YYYY is an integer between 1000 and 2999
""", re.VERBOSE)

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
    """Check if a text is a 'MM-DD-YYYY' formated date and is a valid date.
    """
    if not is_valid_date_in_american_format(text):
        return False

    month, day, year = [int(n) for n in text.split('-')]

    if not (0 < day <= DAYS_IN_MONTHS[month]):
        return False

    if day == 29 and month == 2 and not is_leap_year(year):
        return False

    return True


def is_valid_date_in_american_format(text):
    """Check if a string as a 'MM-DD-YYYY' format.
    """
    return bool(re.search(AMERICAN_DATE_PATTERN, text))

def change_date_format_from_am_to_eu(date):
    if is_valid_date(date):
        month, day, year = date.split("-")
        return f"{day}-{month}-{year}"
    else:
        return f"{date} is not a valid american MM-DD-YYYY formated date."

def change_name_with_date(name):
    for tupled_date in re.findall(AMERICAN_DATE_PATTERN, name):
        month, day, year = tupled_date

        american_date = f'{month}-{day}-{year}'
        european_date = change_date_format_from_am_to_eu(american_date)

        name = name.replace(american_date, european_date)

    return name

def rename_file_with_date(filename):
    new_filename = change_name_with_date(filename)

    if new_filename != filename:
        shutil.move(filename, new_filename)

def rename_files_with_date_in_folder(folder):
    folder_content = os.listdir()

    for filename in folder_content:
        rename_file_with_date(filename)


if __name__ == "__main__":
    pass
