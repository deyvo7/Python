# Convenient processing of CSV documents is possible using the CSV module.
# Find on the Internet how to use this module. Then write a program that, based on the it_company.csv file,
# prints the first name, last name and email (in the given order, without Job Title) of people employed
#  in the position of 'Graphic Designer'. Sample result:

# GRAPHIC DESIGNERS
# =================
# Chris Martin,chris.martin@example.com
# Jane Taylor,jane.taylor@example.com
# ...
# ...

import csv  # Importujemy moduł do pracy z plikami CSV

# Ścieżka do pliku CSV
file_name = 'it_company.csv'

# Otwieramy plik CSV
with open(file_name, 'r', newline='', encoding='utf-8') as file:
    # Tworzymy obiekt reader do odczytu pliku CSV
    reader = csv.reader(file)

    # Pomijamy nagłówki (pierwsza linia pliku)
    header = next(reader)

    # Drukujemy tytuł sekcji
    print("GRAPHIC DESIGNERS")
    print("=================")

    # Iterujemy po każdej linii w pliku
    for row in reader:
        # Sprawdzamy, czy stanowisko to 'Graphic Designer'
        if row[2] == 'Graphic Designer':
            # Wypisujemy imię, nazwisko oraz e-mail (kolumny 1, 0, 3)
            print(f"{row[1]} {row[0]},{row[3]}")
