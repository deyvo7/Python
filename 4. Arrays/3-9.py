# Define a function compare(array1, array2) that returns True if both arrays are the same or False otherwise.
# Two arrays are the same if they have the same number of elements and values of elements in cells of arrays with the same index are equal.
# Then create a program and try to compare the following arrays:

# 1. ["water","book","sky"]   ["water","book","sky"]
# 1. [True,False]   [True,False,True]
# 1. [5,3,1]   [5,3,1]
# 1. [3,2,1]   [3,2]
# Print both arrays and the result of comparison. Sample result:

# Array1: water book sky
# Array2: water book sky
# Comparison: arrays are the same

# Definicja funkcji compare, która porównuje dwie tablice
def compare(array1, array2):
    # Sprawdzamy, czy tablice mają tę samą długość
    # Jeśli długości tablic się różnią, oznacza to, że tablice nie mogą być identyczne
    if len(array1) != len(array2):
        return False  # Zwracamy False, ponieważ tablice nie są takie same

    # Jeśli długości tablic są równe, porównujemy każdy element tablic
    for i in range(len(array1)):  # Iterujemy po wszystkich elementach w tablicy
        if array1[i] != array2[i]:  # Porównujemy elementy o tym samym indeksie
            return False  # Jeśli którykolwiek element się różni, tablice są różne

    # Jeśli nie znaleźliśmy żadnych różnic, zwracamy True
    # To oznacza, że tablice mają tę samą długość i identyczne elementy
    return True

# Lista par tablic do porównania
arrays_to_compare = [
    (["water", "book", "sky"], ["water", "book", "sky"]),  # Przykład tablic identycznych
    ([True, False], [True, False, True]),  # Przykład tablic o różnej długości
    ([5, 3, 1], [5, 3, 1]),  # Przykład identycznych tablic z liczbami
    ([3, 2, 1], [3, 2])  # Przykład tablic o różnych długościach
]

# Przechodzimy przez każdą parę tablic z listy arrays_to_compare
for i, (array1, array2) in enumerate(arrays_to_compare, 1):
    # Wyświetlamy zawartość tablic przed porównaniem
    print(f"Array1: {' '.join(map(str, array1))}")  # Zmieniamy elementy tablicy na ciągi znaków i je wypisujemy
    print(f"Array2: {' '.join(map(str, array2))}")  # Zmieniamy elementy tablicy na ciągi znaków i je wypisujemy
    
    # Wywołujemy funkcję compare, aby sprawdzić, czy tablice są identyczne
    result = compare(array1, array2)

    # Jeśli funkcja compare zwróciła True, tablice są identyczne
    if result:
        print(f"Comparison: arrays are the same")  # Wypisujemy informację, że tablice są takie same
    else:
        print(f"Comparison: arrays are not the same")  # Wypisujemy informację, że tablice są różne
    
    print()  # Pusty wiersz dla lepszej czytelności między wynikami porównań
