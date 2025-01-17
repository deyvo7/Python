# Create a program that computes the second power of each array element. Sample result:

# Array: 8 2 5 1 9
# 2nd power: 64 4 25 1 81


# Tablica wejściowa z wartościami
arr = [8, 2, 5, 1, 9]

# Wyświetlanie oryginalnej tablicy
# 'end=" "' zapobiega przejściu do nowej linii po każdym elemencie
print("Array:", end=" ")
for num in arr:
    print(num, end=" ")  # Wypisuje każdy element z tablicy, oddzielony spacją

# Tworzymy nową tablicę, w której zapisujemy potęgę 2 dla każdego elementu
second_power = []

# Pętla przechodząca przez każdy element tablicy wejściowej
for num in arr:
    second_power.append(num ** 2)  # Dodajemy do nowej tablicy wynik potęgowania (num ** 2)

# Wyświetlanie wyników - tablica zawierająca drugą potęgę każdego elementu
print("\n2nd power:", end=" ")
for num in second_power:
    print(num, end=" ")  # Wypisuje każdy element z nowej tablicy, oddzielony spacją
