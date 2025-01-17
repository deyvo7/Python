# An array contains values: 15, 8, 31, 47, 2, 19. 
# Create a program that calculates and prints the array and the arithmetic mean of array values.
# Use the “while” loop statement.

# Tablica z wartościami
arr = [15, 8, 31, 47, 2, 19]

# Zmienna do przechowywania sumy elementów tablicy
total_sum = 0

# Zmienna do przechowywania indeksu
index = 0

# Pętla while, która przechodzi przez tablicę
while index < len(arr):
    total_sum += arr[index]  # Dodajemy element tablicy do sumy
    index += 1  # Przechodzimy do kolejnego elementu

# Obliczamy średnią arytmetyczną
mean = total_sum / len(arr)  # Suma wszystkich liczb podzielona przez liczbę elementów w tablicy

# Wypisujemy tablicę oraz obliczoną średnią
print("Array:", arr)
print("Arithmetic mean:", mean)
