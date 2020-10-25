"""Script to extract all american phone numbers and emails from a text.
"""


import re


PHONE_PATTERN = re.compile(r'''
    [^\d]*  # no additional digit before
    (\d{3}|\(\d{3}\))?  #area code
    (\s|-|\.)?  # separator
    (\d{3})  # first 3 digits
    (\s|-|\.)  # separator
    (\d{4})  # last 4 digits and no extra digit
''', re.VERBOSE)

MAIL_PATTERN = re.compile(r'''
    [a-zA-Z0-9._%+-]+  #username
    @  # arobase needed
    [a-zA-Z0-9.-]+  # domain name
    \.[a-zA-Z]{2,4}  # extension
''', re.VERBOSE)


def is_valid_phone_number(text):
    return bool(re.search(PHONE_PATTERN, text))

def is_valid_mail(text):
    return bool(re.search(MAIL_PATTERN, text))

def collect_phones(text):
    collected_phones = []

    for groups in re.findall(PHONE_PATTERN, text):
        phone = "-".join([groups[0], groups[2], groups[4]])
        collected_phones.append(phone)

    return collected_phones

def collect_mails(text):
    collect_mails = []

    for mail in re.findall(MAIL_PATTERN, text):
        collect_mails.append(mail)

    return collect_mails


if __name__ == '__main__':
    TEXT = """
Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950

Reach Us by Email

General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Help with your order: info@nostarch.com
Reach Us on Social Media
Twitter
Facebook
Instagram
Linkedin
Pinterest"""

    print(TEXT)

    print("\n--- PHONES COLLECTED ---")
    for phone_number in collect_phones(TEXT):
        print(phone_number)

    print("\n--- MAILS COLLECTED ---")
    for mail in collect_mails(TEXT):
        print(mail)
