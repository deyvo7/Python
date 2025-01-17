# Write a program that displays the first five lines from the it_company.csv file and then
# prints 'Press Enter key...' in the next line and waits for the Enter key to be pressed.
# The program repeats printing the next five lines from the file, waiting for the Enter key to be pressed each time.

# Otwieramy plik z listą pracowników
file_name = 'it_company.csv'

# Funkcja do wyświetlania linii w zestawach po 5
def display_lines_in_sets_of_five(file_name):
    # Otwieramy plik w trybie do odczytu
    with open(file_name, 'r') as file:
        # Odczytujemy wszystkie linie z pliku i zapisujemy je w liście
        lines = file.readlines()

        # Inicjujemy zmienną do śledzenia, od której linii zaczynamy wyświetlanie
        line_number = 0

        # Pętla, która będzie kontynuować wyświetlanie wierszy, dopóki nie wyświetlimy wszystkich
        while line_number < len(lines):
            # Wyświetlamy następne 5 linii z pliku
            for i in range(line_number, min(line_number + 5, len(lines))):
                print(lines[i].strip())  # .strip() usuwa zbędne znaki nowej linii

            # Czekamy na naciśnięcie klawisza Enter przed wyświetleniem kolejnych linii
            input('Naciśnij Enter, aby wyświetlić kolejne linie...')

            # Zaktualizuj numer linii, aby wyświetlić następne 5 linii
            line_number += 5

# Wywołanie funkcji, aby wyświetlić linie z pliku
display_lines_in_sets_of_five(file_name)
