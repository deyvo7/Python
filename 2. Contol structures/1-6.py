###
# Checking whether the number
# entered from the keyboard is even or odd 
#

###
# Sprawdzenie, czy liczba
# wprowadzona z klawiatury jest parzysta czy nieparzysta
###

# Wczytanie liczby od użytkownika
number = int(input('Enter number: '))

# Sprawdzenie, czy liczba jest parzysta
if number % 2 == 0:
    print(f'{number} is even')
else:
    # Jeśli liczba nie jest parzysta, to jest nieparzysta
    print(f'{number} is odd')
