# Define a function occurs(number, array) that returns True if a given number is present in an array.
# Then create a program that checks whether the number entered from the keyboard is present in the array [15, 38, 7, 23, 14].
# 
# Sample result:
# Number: 23
# Array: 15 38 7 23 14
# Result: number 23 appears in the array

# Funkcja sprawdzająca, czy liczba występuje w tablicy
def occurs(number, array):
    # Sprawdzamy, czy liczba znajduje się w tablicy
    if number in array:
        return True
    else:
        return False

# Definiujemy tablicę
array = [15, 38, 7, 23, 14]

# Pobieramy liczbę od użytkownika
number = int(input("Enter a number: "))  # Konwertujemy wejście na liczbę całkowitą

# Sprawdzamy, czy liczba występuje w tablicy
result = occurs(number, array)

# Wypisujemy wynik
print("Number:", number)
print("Array:", end=" ")
for elem in array:
    print(elem, end=" ")

if result:
    print(f"\nResult: number {number} appears in the array")
else:
    print(f"\nResult: number {number} does not appear in the array")
