# An array contains values: 2, 3, 7, 5, 4.
# Write a program that prints:
# the array
# number of elements
# first value
# second value
# last value
# last but one value (do not use negative index values)
# sum of the first and last value
# middle value
# all array values separated by a single space (use a loop statement)

# Tip: to read the last value of an array use array[len(array)-1]
#  or array[-1]

###
# Prints some array elements
#
# Definiujemy tablicę z wartościami
arr = [2, 3, 7, 5, 4]

# Wypisujemy całą tablicę
print("Tablica:", arr)

# Liczba elementów w tablicy
print("Liczba elementów:", len(arr))

# Pierwszy element tablicy
print("Pierwsza wartość:", arr[0])

# Druga wartość w tablicy
print("Druga wartość:", arr[1])

# Ostatnia wartość w tablicy
print("Ostatnia wartość:", arr[len(arr)-1])  # len(arr)-1 to ostatni indeks

# Przedostatnia wartość w tablicy
print("Przedostatnia wartość:", arr[len(arr)-2])

# Suma pierwszej i ostatniej wartości
print("Suma pierwszej i ostatniej wartości:", arr[0] + arr[len(arr)-1])

# Środkowa wartość tablicy
print("Środkowa wartość:", arr[len(arr)//2])  # // oznacza dzielenie całkowite

# Wszystkie wartości tablicy oddzielone spacją
print("Wszystkie wartości oddzielone spacją:")
for i in arr:  # Iterujemy po elementach tablicy
    print(i, end=" ")  # Wypisujemy elementy w jednym wierszu
