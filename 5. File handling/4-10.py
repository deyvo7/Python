# The clothing.csv contains a list of clothing in stock. Write a program that prints those products
#  whose price is less than 60 and whose stock is less than 40.

import csv  # Importujemy moduł do pracy z plikami CSV

# Nazwa pliku CSV
file_name = 'clothing.csv'

# Otwieramy plik CSV w trybie odczytu
with open(file_name, 'r', newline='', encoding='utf-8') as file:
    # Tworzymy obiekt reader do odczytu zawartości pliku CSV
    reader = csv.reader(file)

    # Pomijamy nagłówki (pierwsza linia)
    header = next(reader)

    # Iterujemy przez wszystkie wiersze w pliku CSV
    for row in reader:
        # Odczytujemy cenę (index 5) i ilość (index 6) jako liczby
        price = float(row[5])  # Cena produktu
        stock = int(row[6])    # Ilość w magazynie

        # Sprawdzamy, czy cena jest mniejsza niż 60 i ilość w magazynie mniejsza niż 40
        if price < 60 and stock < 40:
            # Jeśli warunki są spełnione, drukujemy nazwę produktu, cenę i ilość
            print(f"Product: {row[1]}, Price: {price}, Stock: {stock}")
