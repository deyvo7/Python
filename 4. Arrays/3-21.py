# Write a program that checks whether the first array is a subset of the second one
# (whether all elements of the first array appear in the second array).

# Funkcja, która sprawdza, czy pierwsza tablica jest podzbiorem drugiej
def is_subset(arr1, arr2):
    for element in arr1:  # Dla każdego elementu w pierwszej tablicy
        if element not in arr2:  # Sprawdzamy, czy element nie występuje w drugiej tablicy
            return False  # Jeśli któryś element nie występuje w drugiej tablicy, zwracamy False
    return True  # Jeśli wszystkie elementy pierwszej tablicy występują w drugiej, zwracamy True

# Przykład użycia
arr1 = [2, 4, 5]  # Pierwsza tablica
arr2 = [1, 2, 3, 4, 5, 6]  # Druga tablica

# Sprawdzamy, czy arr1 jest podzbiorem arr2
if is_subset(arr1, arr2):
    print("Pierwsza tablica jest podzbiorem drugiej.")
else:
    print("Pierwsza tablica nie jest podzbiorem drugiej.")
