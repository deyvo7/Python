# Create a function transpose_matrix(m) that returns transposed matrix m:

# https://en.wikipedia.org/wiki/Transpose

# Then, create a program that prints transposed matrices, in rows and columns, for the following matrices.

# 1 2 3
# 4 5 6
# 7 8 9
# 1 2 3 4 5
# 6 7 8 9 0
# 5 6 7 8


# Funkcja do transponowania macierzy
def transpose_matrix(m):
    # Tworzymy pustą macierz, w której będziemy przechowywać transponowane wartości
    transposed = []
    
    # Iterujemy przez kolumny macierzy
    for j in range(len(m[0])):  # Dla każdej kolumny
        new_row = []  # Tworzymy nowy wiersz
        for i in range(len(m)):  # Dla każdego wiersza w kolumnie
            new_row.append(m[i][j])  # Dodajemy odpowiedni element
        transposed.append(new_row)  # Dodajemy wiersz do transponowanej macierzy

    return transposed

# Funkcja do wypisania macierzy w formie tabeli
def print_matrix(matrix):
    # Iterujemy przez każdy wiersz macierzy
    for row in matrix:
        # Wypisujemy każdy wiersz w formie ciągu znaków, oddzielając elementy spacją
        print(' '.join(map(str, row)))

# Przykładowe macierze
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix3 = [
    [5, 6, 7, 8]
]

# Wypisanie transponowanych macierzy
print("Transponowana macierz 1:")
print_matrix(transpose_matrix(matrix1))

print("\nTransponowana macierz 2:")
print_matrix(transpose_matrix(matrix2))

print("\nTransponowana macierz 3:")
print_matrix(transpose_matrix(matrix3))
