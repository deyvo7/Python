###
# Checking login and password
#
###
# Sprawdzanie loginu i hasła
###

# Zdefiniuj poprawny login i hasło
login = 'joe'  # Poprawny login
password = 'abcd'  # Poprawne hasło

# Pobierz login i hasło od użytkownika
entered_login = input('Login: ')  # Użytkownik wpisuje swój login
entered_password = input('Password: ')  # Użytkownik wpisuje swoje hasło

# Sprawdź, czy login i hasło wprowadzone przez użytkownika są poprawne
if login == entered_login and password == entered_password:
    print('You are logged in')  # Jeśli login i hasło są poprawne, wyświetl komunikat o zalogowaniu
else:
    print('Incorrect login or password!!')  # W przeciwnym razie wyświetl komunikat o błędzie
