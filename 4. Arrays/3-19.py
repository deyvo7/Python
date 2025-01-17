# Write a program that, for the given array of real numbers, 
# prints the number of elements that are greater than the given value entered from the keyboard.

# Funkcja, która zlicza elementy większe od podanej wartości
def count_greater_than(arr, value):
    count = 0  # Inicjalizujemy licznik
    for num in arr:  # Przechodzimy po wszystkich elementach tablicy
        if num > value:  # Sprawdzamy, czy element jest większy od podanej wartości
            count += 1  # Jeżeli tak, inkrementujemy licznik
    return count  # Zwracamy końcowy wynik

# Program główny
# Wczytujemy tablicę liczb zmiennoprzecinkowych
numbers = [3.5, 7.2, 1.3, 9.8, 4.6, 2.0, 8.4]  # Przykładowa tablica liczb

# Wczytujemy liczbę graniczną z klawiatury
value = float(input("Enter the value to compare: "))

# Zliczamy i wyświetlamy wynik
result = count_greater_than(numbers, value)
print(f"Number of elements greater than {value}: {result}")
