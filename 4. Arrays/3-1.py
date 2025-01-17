# An array contains integer numbers: 34,7,19,4,21,8. Create a program that calculates and prints
# the number of even values in the array. Use the ‘while’ loop statement.

# Tablica z liczbami całkowitymi
numbers = [34, 7, 19, 4, 21, 8]

# Inicjalizacja zmiennej do liczenia liczb parzystych
even_count = 0

# Inicjalizujemy indeks, który będziemy używać w pętli while
i = 0

# Pętla while, która przechodzi przez wszystkie elementy tablicy
while i < len(numbers):
    # Sprawdzamy, czy liczba jest parzysta
    if numbers[i] % 2 == 0:
        # Jeśli liczba jest parzysta, zwiększamy licznik
        even_count += 1
    # Zwiększamy indeks, aby przejść do następnej liczby
    i += 1

# Wypisujemy wynik
print("Liczba liczb parzystych w tablicy:", even_count)
