# An array contains integer numbers: 2, 6, 4, 9, 7. Create a program that prints the array values graphically as below.
#  Define a function star(n) that returns the given number of asterisks as a string. Use a defined function in the program.

# 2: **
# 6: ******
# 4: ****
# 9: *********
# 7: *******

# Definicja funkcji star, która zwraca ciąg gwiazdek o długości n
def star(n):
    return '*' * n  # Zwracamy ciąg gwiazdek o długości n

# Tablica z liczbami całkowitymi
numbers = [2, 6, 4, 9, 7]

# Przechodzimy przez tablicę i dla każdego elementu wypisujemy liczbę oraz odpowiednią ilość gwiazdek
for num in numbers:
    print(f"{num}: {star(num)}")  # Wywołanie funkcji star i wypisanie liczby oraz gwiazdek
