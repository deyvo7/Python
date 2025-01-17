# Importujemy funkcję reduce z modułu functools
from functools import reduce

# Funkcja anonimowa (lambda) do dodawania dwóch liczb
# Zastępujemy tradycyjną funkcję add(x, y) funkcją lambda, która dodaje dwie liczby
add = lambda x, y: x + y

# Lista liczb, które chcemy dodać
numbers = [1, 2, 3, 4, 5]

# Używamy funkcji reduce, aby zredukować listę liczb do jednej liczby
# Funkcja reduce iteruje po wszystkich elementach listy i stosuje funkcję add (lambda) do obliczania sumy
result = reduce(add, numbers)

# Wypisujemy wynik - suma liczb w liście
print(result)  # Oczekiwany wynik: 15
