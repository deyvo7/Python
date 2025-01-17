# The following array represents a square matrix and contains values:

# Macierz 3x3, w której wszystkie elementy są początkowo ustawione na 0
matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]

# Pętla, która przechodzi przez każdy wiersz (a zarazem każdą kolumnę)
# Główną ideą jest, że na głównej diagonali (gdzie i == j) zamieniamy 0 na 1.
for i in range(len(matrix)):
    # Zamiana wartości na głównej diagonali (matrix[i][i]) z 0 na 1
    matrix[i][i] = 1

# Pętla do drukowania zmodyfikowanej macierzy.
# Dla każdej linii (wiersza) w macierzy drukujemy wszystkie wartości w tej linii.
for row in matrix:
    # Dla każdego elementu w bieżącym wierszu (row) drukujemy go,
    # a "end=' '" powoduje, że wartości są oddzielone spacjami, a nie nowymi liniami.
    for value in row:
        print(value, end=" ")
    # Po wydrukowaniu całego wiersza przechodzimy do nowej linii
    print()

