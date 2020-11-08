"""Basic script to retrieve emails.
"""

import pprint
import sys

import imapclient
import pyzmail

from settings import (
    IMAP_SERVER,
    RETRIEVED_MAIL,
)


if __name__ == '__main__':
    # To allow SSL connection:
    #   - browse to Applications/Python 3.X
    #   - double-click 'Install Certificates.command'
    imap_connection = imapclient.IMAPClient(IMAP_SERVER, ssl=True)
    print(imap_connection)

    retrieved_mail_password = input(
        f"Entrez le mot de passe pour {RETRIEVED_MAIL} : "
    )
    try:
        mail_response = imap_connection.login(
            RETRIEVED_MAIL, retrieved_mail_password,
        )
        print(mail_response)

    except imapclient.exceptions.LoginError:
        print("Mot de passe erroné")
        sys.exit()

    retrieved_mail_folders = imap_connection.list_folders()
    pprint.pprint(retrieved_mail_folders)

    imap_connection.select_folder('INBOX', readonly=True)

    unread_mails_uids = imap_connection.search(['UNSEEN'])
    raw_mails = imap_connection.fetch(unread_mails_uids, ['BODY[]'])

    last_unread_mail_uid = unread_mails_uids[-1]
    last_unread_mail = pyzmail.PyzMessage.factory(
        raw_mails[last_unread_mail_uid][b'BODY[]']
    )
    pprint.pprint(last_unread_mail)

    mail_subject = last_unread_mail.get_subject()
    mail_from = last_unread_mail.get_addresses('from')
    mail_to = last_unread_mail.get_addresses('to')

    print(f"""
    SUBJECT: {mail_subject}
    FROM: {mail_from}
    TO: {mail_to}
    """)

    if last_unread_mail.text_part:
        print("--- TEXT CONTENT ---")
        text = last_unread_mail.text_part.get_payload().decode(
            last_unread_mail.text_part.charset
        )
        print(f"{text[:500]}...")
    if last_unread_mail.html_part:
        print("--- HTML CONTENT ---")
        html = last_unread_mail.html_part.get_payload().decode(
            last_unread_mail.html_part.charset
        )
        print(f"{html[:500]}...")

    imap_connection.logout()
