# Importujemy funkcję reduce z modułu functools
from functools import reduce

# Lista liczb, z których chcemy wybrać liczby parzyste i obliczyć ich sumę
numbers = [2, 4, 6, 3, 7, 5]

# Używamy funkcji filter() do wybrania tylko liczb parzystych z listy
# Funkcja lambda sprawdza, czy liczba jest parzysta (x % 2 == 0)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Używamy funkcji reduce() do obliczenia sumy liczb parzystych
# Funkcja lambda dodaje kolejne liczby z listy
sum_even = reduce(lambda x, y: x + y, even_numbers)

# Wypisujemy wynik - suma liczb parzystych
print(f"Sum of even numbers: {sum_even}")  # Oczekiwany wynik: 12
