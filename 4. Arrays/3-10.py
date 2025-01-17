# Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36].
# Create a program that prints the numbers from the first array that do not appear in the second array.

# Pierwsza tablica zawiera liczby
array1 = [4, 36, 12, 28, 9, 44, 5]

# Druga tablica zawiera liczby
array2 = [5, 1, 36]

# Pętla, która iteruje po elementach pierwszej tablicy
for number in array1:
    # Sprawdzamy, czy element z array1 nie znajduje się w array2
    if number not in array2:
        print(number)  # Jeśli liczba nie występuje w array2, wypisujemy ją
