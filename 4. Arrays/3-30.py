# An array contains values:

# [[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
# Create a program that modifies the array values to create a multiplication table as below. Use loop statements. Print the array.

# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25

# Funkcja do tworzenia tablicy mnożenia 5x5
def multiplication_table():
    # Tworzymy pustą tablicę 5x5
    table = []
    
    # Wypełniamy tablicę wartościami
    for i in range(1, 6):  # i to numer wiersza (od 1 do 5)
        row = []  # Tworzymy pusty wiersz
        for j in range(1, 6):  # j to numer kolumny (od 1 do 5)
            row.append(i * j)  # Dodajemy wynik mnożenia do wiersza
        table.append(row)  # Dodajemy wiersz do tablicy
    
    return table

# Tworzymy tablicę mnożenia
table = multiplication_table()

# Wypisujemy tablicę z odpowiednim formatowaniem
for row in table:
    # Formatowanie: każda liczba w wierszu ma szerokość 4 znaków
    print(" ".join(f"{num:4}" for num in row))
