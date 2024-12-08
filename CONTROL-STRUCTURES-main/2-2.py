###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
###
# Program do sprawdzania rozmiarów odzieży
# S: rozmiar mały, M: rozmiar średni, L: rozmiar duży
# XL: rozmiar extra duży lub Nieprawidłowy symbol (jeśli wprowadzono symbol
# inny niż S, M, L, XL)
###

# Wczytanie symbolu rozmiaru od użytkownika
size = input('Enter size symbol: ')

# Sprawdzenie, jaki rozmiar został podany i wypisanie odpowiedniego komunikatu
if size == 'S':
    print('S: Small size')
elif size == 'M':
    print("M: Medium size")
elif size == 'L':
    print("L: Large size")
elif size == 'XL':
    print("XL: Large size")
else:
    # Wypisanie komunikatu, jeśli symbol jest nieprawidłowy
    print("Incorrect symbol")
