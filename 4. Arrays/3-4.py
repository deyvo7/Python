# An array contains numbers: -15, 8, -31, 47, -2, 19.
#  Create a program that finds and prints the maximum and minimum number.
# Do not use available functions.

# Tablica wejściowa zawierająca liczby
arr = [-15, 8, -31, 47, -2, 19]

# Inicjalizujemy zmienne do przechowywania maksymalnej i minimalnej liczby.
# Początkowo ustawiamy pierwszą liczbę z tablicy jako zarówno maksymalną, jak i minimalną.
max_num = arr[0]
min_num = arr[0]

# Pętla przechodząca przez każdy element tablicy
for num in arr:
    # Sprawdzamy, czy aktualny element jest większy niż dotychczasowy maksymalny
    if num > max_num:
        max_num = num  # Jeśli tak, aktualizujemy wartość maksymalną
    
    # Sprawdzamy, czy aktualny element jest mniejszy niż dotychczasowy minimalny
    if num < min_num:
        min_num = num  # Jeśli tak, aktualizujemy wartość minimalną

# Wyświetlanie wyników
print("Maximum number:", max_num)
print("Minimum number:", min_num)
