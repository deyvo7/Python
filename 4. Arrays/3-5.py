# An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and prints
# the array and the arithmetic mean of array values. Use the “for” loop statement.

# Tablica z wartościami
arr = [15, 8, 31, 47, 2, 19]

# Zmienna do przechowywania sumy elementów tablicy
total_sum = 0

# Pętla for przechodząca przez wszystkie elementy tablicy
for num in arr:
    total_sum += num  # Dodajemy każdą liczbę do sumy

# Obliczamy średnią arytmetyczną
mean = total_sum / len(arr)  # Suma wszystkich liczb podzielona przez liczbę elementów w tablicy

# Wypisujemy tablicę oraz obliczoną średnią
print("Array:", arr)
print("Arithmetic mean:", mean)
