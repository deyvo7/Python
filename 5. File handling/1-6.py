# The following program prints a list of countries from 'countries.txt' file.
# Modify the program to print a list of countries sorted alphabetically.

# Tip. Before printing the contents of the array,
# sort it alphabetically using the built-in function sorted()



# Funkcja, która odczytuje całą zawartość pliku
def read_from_file(name):
    # Otwieramy plik w trybie do odczytu ('r')
    with open(name, 'r') as file:
        # Odczytujemy całą zawartość pliku jako jeden długi ciąg znaków
        content = file.read()
    # Zwracamy zawartość pliku
    return content

# Wywołanie funkcji, która odczytuje zawartość pliku 'countries.txt'
file_content = read_from_file('countries.txt')

# Metoda splitlines() dzieli tekst na listę linii. Każda linia staje się osobnym elementem w liście
# Na przykład: jeśli plik zawiera 3 kraje w 3 liniach, to powstaje lista: ['Polska', 'Niemcy', 'Francja']
file_lines = file_content.splitlines()

# Funkcja sorted() sortuje listę alfabetycznie. Tworzymy nową posortowaną listę
file_lines_sorted = sorted(file_lines)

# Pętla, która przechodzi przez każdy element (kraj) w posortowanej liście
# I wypisuje go na ekranie
for line in file_lines_sorted:
    # Wypisujemy każdy kraj (linia) w posortowanej liście
    print(line)
