# An array contains natural numbers: 15, 8, 31, 47, 2, 19.
# Create a program that prints the contents of the array in reverse order.
# Use any loop statement. Sample result:

# existed array: 15 8 31 47 2 19 
# reverse array: 19 2 47 31 8 15

# Tablica z liczbami całkowitymi - są to liczby naturalne
numbers = [15, 8, 31, 47, 2, 19]

# Wypisujemy oryginalną tablicę
# Używamy pętli, aby wypisać każdy element tablicy
print("Oryginalna tablica:", end=" ")
for number in numbers:
    print(number, end=" ")

# Pętla przechodząca przez tablicę od końca do początku
print("\nTablica w odwrotnej kolejności:", end=" ")
for i in range(len(numbers)-1, -1, -1):  # Pętla idzie od ostatniego elementu do pierwszego
    print(numbers[i], end=" ")
