# In mathematics, a matrix is a rectangular array or table of numbers, symbols, or expressions, arranged in rows and columns, e.g.:

# -7  12 38
# 41 -19 11
# Create a function identity_matrix(n) that returns an identity matrix(2D array) of size n.

# https://en.wikipedia.org/wiki/Identity_matrix

# Then, create a function that prints a 2D array in rows and columns.
# Finally, create a program that prints three identity matrices with dimensions of 3, 5 and 8.

# Sample result:
# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1

# Funkcja do tworzenia macierzy jednostkowej o wymiarach n
def identity_matrix(n):
    # Tworzymy pustą listę, która będzie przechowywać naszą macierz
    matrix = []
    
    # Pętla do przechodzenia przez każdy wiersz macierzy
    for i in range(n):
        # Tworzymy pustą listę dla każdego wiersza
        row = []
        
        # Pętla do przechodzenia przez każdą kolumnę w wierszu
        for j in range(n):
            # Sprawdzamy, czy indeks wiersza (i) i indeks kolumny (j) są takie same
            if i == j:
                # Jeśli są takie same, to wstawiamy '1' na przekątnej (macierz jednostkowa)
                row.append(1)
            else:
                # Jeśli są różne, to wstawiamy '0'
                row.append(0)
        
        # Po zakończeniu pętli wewnętrznej dodajemy cały wiersz do macierzy
        matrix.append(row)
    
    # Zwracamy gotową macierz
    return matrix

# Funkcja do wypisywania macierzy
def print_matrix(matrix):
    # Pętla do przechodzenia przez każdy wiersz w macierzy
    for row in matrix:
        # Łączymy elementy wiersza w jeden ciąg znaków, oddzielając je spacjami
        # map(str, row) zamienia każdą liczbę w wierszu na tekst
        # ' '.join() łączy te teksty spacjami
        print(' '.join(map(str, row)))

# Program główny, który wypisuje trzy macierze jednostkowe o różnych wymiarach
print("Macierz jednostkowa o wymiarach 3:")
# Tworzymy macierz jednostkową o wymiarach 3x3 i drukujemy ją
print_matrix(identity_matrix(3))

print("\nMacierz jednostkowa o wymiarach 5:")
# Tworzymy macierz jednostkową o wymiarach 5x5 i drukujemy ją
print_matrix(identity_matrix(5))

print("\nMacierz jednostkowa o wymiarach 8:")
# Tworzymy macierz jednostkową o wymiarach 8x8 i drukujemy ją
print_matrix(identity_matrix(8))
