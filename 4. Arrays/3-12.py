# Create a program that prints all unique elements in an array. Sample result:

# Array: 2 3 2 5 8 1 9 8
# Unique elements: 3 5 1 9

# Definicja tablicy z wartościami
array = [2, 3, 2, 5, 8, 1, 9, 8]

# Tworzymy pustą tablicę, która będzie przechowywać unikalne elementy
unique_elements = []

# Zewnętrzna pętla, która przechodzi przez każdy element tablicy
for element in array:
    # Jeśli element występuje tylko raz w tablicy (liczymy jego wystąpienia)
    if array.count(element) == 1:
        # Dodajemy go do tablicy unikalnych elementów
        unique_elements.append(element)

# Wypisujemy oryginalną tablicę
print("Array:", end=" ")
for elem in array:
    print(elem, end=" ")  # Wypisuje każdy element tablicy z pojedynczym odstępem

# Wypisujemy unikalne elementy
print("\nUnique elements:", end=" ")
for elem in unique_elements:
    print(elem, end=" ")  # Wypisuje unikalne elementy tablicy z pojedynczym odstępem
