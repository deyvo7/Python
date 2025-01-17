# Try to create the following arrays. Then, print the created array content.

import random  # Importujemy moduł random, aby móc generować losowe liczby

# Tworzenie tablic zgodnie z opisem

# arr1: Lista zawierająca 5 elementów [3,7,1,0,4]
arr1 = [3, 7, 1, 0, 4]

# arr2: Dwuwymiarowa lista (macierz) zawierająca trzy wiersze, po dwa elementy w każdym wierszu
arr2 = [[2, 3], [7, 1], [0, 4]]

# arr3: Lista, w której wszystkie 5 elementów to liczba 7
arr3 = []
for i in range(5):
    arr3.append(7)  # Dodajemy 7 pięć razy

# arr4: Lista zawierająca liczby od 1 do 9
arr4 = []
for i in range(1, 10):
    arr4.append(i)  # Dodajemy liczby od 1 do 9

# arr5: Lista zawierająca liczby będące wielokrotnościami 2
arr5 = []
for i in range(1, 10):
    arr5.append(i * 2)  # Dodajemy kolejne liczby będące wielokrotnościami 2

# arr6: Lista 10 losowych liczb z zakresu od 1 do 20
arr6 = []
for i in range(10):
    arr6.append(random.randint(1, 20))  # Generujemy losowe liczby z zakresu 1-20

# arr7: Lista zawierająca 5 pustych list
arr7 = []
for i in range(5):
    arr7.append([])  # Dodajemy pustą listę 5 razy

# arr8: Dwuwymiarowa lista (macierz) 4 wiersze, po 2 kolumny wypełnione liczbą 1
arr8 = []
for j in range(4):
    inner_list = []  # Tworzymy pustą listę wewnętrzną
    for i in range(2):
        inner_list.append(1)  # Dodajemy do wewnętrznej listy liczbę 1
    arr8.append(inner_list)  # Dodajemy listę do głównej listy

# arr9: Dwuwymiarowa lista (macierz) zawierająca 5 wierszy i 3 kolumny, wypełniona losowymi liczbami od 1 do 20
arr9 = []
for j in range(5):
    inner_list = []  # Tworzymy pustą listę wewnętrzną
    for i in range(3):
        inner_list.append(random.randint(1, 20))  # Generujemy losowe liczby z zakresu 1-20
    arr9.append(inner_list)  # Dodajemy listę do głównej listy

# Teraz wypisujemy zawartość tablic

print("arr1:", arr1)  # Wypisujemy arr1
print("arr2:", arr2)  # Wypisujemy arr2
print("arr3:", arr3)  # Wypisujemy arr3
print("arr4:", arr4)  # Wypisujemy arr4
print("arr5:", arr5)  # Wypisujemy arr5
print("arr6:", arr6)  # Wypisujemy arr6
print("arr7:", arr7)  # Wypisujemy arr7
print("arr8:", arr8)  # Wypisujemy arr8
print("arr9:", arr9)  # Wypisujemy arr9

# Dodatkowe tablice, które trzeba stworzyć:

# arr10: Tablica zawierająca 3 elementy: [4, 0, 3]
arr10 = [4, 0, 3]
print("arr10:", arr10)  # Wypisujemy arr10

# arr11: Tablica zawierająca 15 elementów, wszystkie to 0
arr11 = []
for i in range(15):
    arr11.append(0)  # Dodajemy 0 piętnaście razy
print("arr11:", arr11)  # Wypisujemy arr11

# arr12: Tablica zawierająca 10 losowych liczb z zakresu 1-30
arr12 = []
for i in range(10):
    arr12.append(random.randint(1, 30))  # Generujemy losowe liczby z zakresu 1-30
print("arr12:", arr12)  # Wypisujemy arr12

# arr13: Tablica zawierająca 20 losowych wartości 0 lub 1
arr13 = []
for i in range(20):
    arr13.append(random.choice([0, 1]))  # Wybieramy losowo 0 lub 1
print("arr13:", arr13)  # Wypisujemy arr13

# arr14: Dwuwymiarowa lista (macierz) o 5 wierszach i 2 kolumnach, wypełniona wartościami False
arr14 = []
for j in range(5):
    inner_list = []  # Tworzymy pustą listę wewnętrzną
    for i in range(2):
        inner_list.append(False)  # Dodajemy do wewnętrznej listy wartość False
    arr14.append(inner_list)  # Dodajemy listę do głównej listy
print("arr14:", arr14)  # Wypisujemy arr14
