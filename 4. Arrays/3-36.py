# Create a function that convert two-dimensional (2D) array into 1D. Then create a program that prints 1D array for the following 2D arrays.

# 2 3
# 1 5
# 5 0 3 7 5
# 9 0 9 1 2
# 2 1
# 3 5
# 7 4
# 2 6

# Funkcja do konwersji 2D na 1D
def convert_to_1d(array_2d):
    # Tworzymy pustą listę 1D
    array_1d = []
    
    # Iterujemy przez każdy wiersz w tablicy 2D
    for row in array_2d:
        # Dodajemy elementy wiersza do listy 1D
        array_1d.extend(row)
    
    return array_1d

# Funkcja do wypisania tablicy
def print_array(array):
    print(" ".join(map(str, array)))

# Przykładowe dwuwymiarowe tablice
array1 = [
    [2, 3],
    [1, 5]
]

array2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

array3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# Wypisanie tablic 1D
print("Tablica 1D z array1:")
print_array(convert_to_1d(array1))

print("\nTablica 1D z array2:")
print_array(convert_to_1d(array2))

print("\nTablica 1D z array3:")
print_array(convert_to_1d(array3))
