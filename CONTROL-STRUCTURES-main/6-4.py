# Password length has a significant impact on the level of data protection.
# Write a program that checks whether the new password provided is at least 12 characters long.

###
# Password validator
# New password is at least 12 characters long
#
###
# Walidator hasła
# Sprawdza, czy nowe hasło ma co najmniej 12 znaków
###

# Pobieranie nowego hasła od użytkownika
new_password = input('Enter new password: ')

# Sprawdzanie długości hasła
if len(new_password) < 12:
    # Jeśli hasło jest krótsze niż 12 znaków, wyświetla komunikat o błędzie
    print('Password too short (min. 12 chars).') 
else:
    # Jeśli hasło ma co najmniej 12 znaków, informuje, że hasło jest poprawne
    print("Password is correct.")
