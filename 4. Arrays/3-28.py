# A two-dimensional array contains the following numbers:

# 7 3 7 9 0
# 2 9 0 1 5
# 3 8 6 4 7
# 8 7 1 1 5

# Create a program that calculates the sum of values in the last column.


# Tworzymy dwuwymiarową tablicę
array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

# Inicjalizujemy zmienną do przechowywania sumy
sum_last_column = 0

# Przechodzimy przez każdy wiersz tablicy
for row in array:
    # Dodajemy wartość ostatniej kolumny (indeks -1) do sumy
    sum_last_column += row[-1]

# Drukujemy wynik
print("Suma wartości w ostatniej kolumnie:", sum_last_column)
