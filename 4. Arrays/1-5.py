# An array contains values: 1, 2, 3, 4, 5.
# Write a program that modifies the array values.
# Print the array after each change.

# subtract one from the first element of the array
# increase the last array element by 4
# multiple the middle array element by 2
# Sample result:
# Array: [1,2,3,4,5]
# Array: [0,2,3,4,5]
# Array: [0,2,3,4,9]
# Array: [0,2,6,4,9]

# Definiujemy tablicę z wartościami
arr = [1, 2, 3, 4, 5]

# Wypisujemy początkową tablicę
print("Tablica:", arr)

# Odejmujemy 1 od pierwszego elementu tablicy
arr[0] = arr[0] - 1  # Pierwszy element ma indeks 0
print("Po odjęciu 1 od pierwszego elementu:", arr)

# Dodajemy 4 do ostatniego elementu tablicy
arr[len(arr) - 1] = arr[len(arr) - 1] + 4  # Ostatni element to indeks len(arr)-1
print("Po dodaniu 4 do ostatniego elementu:", arr)

# Mnożymy środkowy element tablicy przez 2
arr[len(arr) // 2] = arr[len(arr) // 2] * 2  # Środkowy element dla nieparzystej długości to len(arr)//2
print("Po pomnożeniu środkowego elementu przez 2:", arr)
