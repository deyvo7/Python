# The file email.txt contains a raw email. Write a program that uses regular expressions to fetch and print:

# sender email address
# recipient email address
# email subject
# email body

# For each of the above commands, define a separate function (see below) that returns
#  the value read from the email. Place the functions in a separate module called emails.

# email_sender()
# email_recipient()
# email_subject()
# email_body()

import emails  # moduł emails.py

# Otwórz plik z e-mailem
email_file = 'email.txt'

with open(email_file, 'r', encoding='utf-8') as file:
    email_content = file.read()

# Wydrukuj wyniki wywołań funkcji
print("Adres nadawcy:", emails.email_sender(email_content))
print("Adres odbiorcy:", emails.email_recipient(email_content))
print("Temat:", emails.email_subject(email_content))
print("Treść wiadomości:", emails.email_body(email_content))

