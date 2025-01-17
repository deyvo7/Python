# Define a function rand_elem(array) that returns a randomly selected array element.
#  Using the function, print a few randomly selected array elements.

import random  # Importujemy moduł random, aby użyć funkcji choice()

# Funkcja, która zwraca losowy element z tablicy
def rand_elem(array):
    return random.choice(array)  # Wybiera losowy element z tablicy

# Przykładowa tablica
arr = [5, 10, 15, 20, 25, 30]

# Wydrukuj kilka losowych elementów z tablicy
print("Losowy element 1:", rand_elem(arr))
print("Losowy element 2:", rand_elem(arr))
print("Losowy element 3:", rand_elem(arr))
