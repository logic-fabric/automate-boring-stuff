"""Basic script to send a email.
"""


import smtplib

from settings import (
    RECIPIENT_MAIL,
    SENDER_MAIL,
    SMTP_OUTPUT_PORT,
    SMTP_SERVER,
    SUBJECT_AND_BODY,
)


if __name__ == '__main__':
    smtp_connection = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_OUTPUT_PORT)

    hello_response = smtp_connection.ehlo()
    print(hello_response)

    sender_password = input(f"Entrez le mot de passe pour {SENDER_MAIL} : ")

    try:
        mail_response = smtp_connection.login(SENDER_MAIL, sender_password)
        print(mail_response)
        
        sending_response = smtp_connection.sendmail(
            SENDER_MAIL,
            RECIPIENT_MAIL,
            SUBJECT_AND_BODY,
        )
        print(sending_response)

    except smtplib.SMTPAuthenticationError:
        print("Mot de passe erroné")
    
    quit_response = smtp_connection.quit()
    print(quit_response)
