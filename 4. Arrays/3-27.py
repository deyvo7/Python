# A two-dimensional array of size 2 by 4 contains integer numbers. Create a program that prints array values in rows and columns.

# Tworzymy dwuwymiarową tablicę 2x4
array = [
    [1, 2, 3, 4],  # Pierwszy wiersz
    [5, 6, 7, 8]   # Drugi wiersz
]

# Przechodzimy przez tablicę i drukujemy każdy wiersz
for row in array:
    # Dla każdego wiersza, drukujemy jego elementy w tej samej linii
    for column in row:
        print(column, end=" ")
    print()  # Przechodzimy do nowej linii po wydrukowaniu wiersza
