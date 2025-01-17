# Many applications require that you create an account with a username
# and password to use them. Often, applications specify requirements for
# the username and password. Write a program that checks whether a username
# and password entered from the keyboard meet the requirements below.
# Use regular expressions.

# username is at least 6 characters long
# username contains only lowercase letters
# password is at least 8 characters long
# password contains only letters (lowercase and uppercase),
# numbers, and the underscore character

import re

# Pobieramy nazwę użytkownika i hasło z klawiatury
username = input("Enter your username: ")
password = input("Enter your password: ")

# Wzorzec (kryteria) dla nazwy użytkownika
# ^ - oznacza początek ciągu
# [a-z] - oznacza, że akceptowane są tylko małe litery od 'a' do 'z'
# {6,} - oznacza, że ciąg musi mieć co najmniej 6 znaków (więcej niż 5 znaków)
# $ - oznacza koniec ciągu
# Cały wzorzec sprawdza, czy nazwa użytkownika składa się tylko z małych liter i ma co najmniej 6 znaków.
username_pattern = r"^[a-z]{6,}$"

# Wzorzec (kryteria) dla hasła
# ^ - oznacza początek ciągu
# [a-zA-Z0-9_] - oznacza, że dozwolone są małe i duże litery, cyfry oraz znak podkreślenia ('_')
# {8,} - oznacza, że hasło musi mieć co najmniej 8 znaków
# $ - oznacza koniec ciągu
# Cały wzorzec sprawdza, czy hasło składa się tylko z liter, cyfr i podkreślenia oraz ma co najmniej 8 znaków.
password_pattern = r"^[a-zA-Z0-9_]{8,}$"

# Sprawdzamy, czy nazwa użytkownika pasuje do wzorca
username_match = re.match(username_pattern, username)

# Sprawdzamy, czy hasło pasuje do wzorca
password_match = re.match(password_pattern, password)

# Jeśli zarówno nazwa użytkownika, jak i hasło pasują do wzorców, wyświetlamy, że są poprawne
if password_match and username_match:
    print("The password and the username are correct.")
else:
    print("There is a problem with your password or username.")
