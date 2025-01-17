# Definiujemy anonimową funkcję (lambda), która zwraca pierwsze litery imienia i nazwiska
# Funkcja przyjmuje dwa argumenty: name (imię) i surname (nazwisko)
# Zwraca złączenie pierwszej litery imienia oraz pierwszej litery nazwiska
initials = lambda name, surname: name[0] + surname[0]

# Pobieramy imię od użytkownika
name = input("Enter the name: ")

# Pobieramy nazwisko od użytkownika
surname = input("Enter the surname: ")

# Wywołujemy funkcję initials(), aby otrzymać pierwsze litery imienia i nazwiska
# Funkcja zwróci dwie pierwsze litery, które są następnie wypisywane na ekranie
print(initials(name, surname))
