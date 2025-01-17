# A two-dimensional array of the size 3 by 5 contains integer numbers.
#  Create a program that swaps the first and the last row.
# Print array values in rows and columns before and after changes.


# Tworzymy dwuwymiarową tablicę o rozmiarze 3x5 z liczbami całkowitymi
tablica = [
    [1, 2, 3, 4, 5],  # Pierwszy wiersz
    [6, 7, 8, 9, 10], # Drugi wiersz
    [11, 12, 13, 14, 15] # Trzeci wiersz
]

# Funkcja do wyświetlania tablicy w formie wierszy i kolumn
def wypisz_tablice(arr):
    for wiersz in arr:  # Dla każdego wiersza w tablicy
        print(wiersz)  # Wypisujemy wiersz

# Wypisujemy tablicę przed zamianą wierszy
print("Tablica przed zamianą:")
wypisz_tablice(tablica)

# Zamieniamy pierwszy i ostatni wiersz w tablicy
tablica[0], tablica[2] = tablica[2], tablica[0]

# Wypisujemy tablicę po zamianie wierszy
print("\nTablica po zamianie:")
wypisz_tablice(tablica)
