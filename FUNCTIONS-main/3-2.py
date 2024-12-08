# Write a program that generates and prints a random number between 1 and 6, similar to rolling a dice.
# Use one of the functions from the random module to generate a random integer within a given range.

###
# Generates and prints a random number between 1 and 6,
# similar to rolling a dice
#


# Importuje moduł random, który umożliwia generowanie liczb losowych
import random

# Generuje losową liczbę całkowitą od 1 do 6 i ją wypisuje
# Funkcja random.randint(a, b) zwraca losową liczbę całkowitą z zakresu od a do b, włącznie
print(random.randint(1, 6))
