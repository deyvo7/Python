# The files.txt contains a list of file names. Write a program that prints only those file names
# whose extensions consist of exactly four characters (e.g. .html).

# Otwieramy plik z nazwami plików
with open('files.txt', 'r') as file:
    # Odczytujemy zawartość pliku i dzielimy na linie
    file_names = file.read().splitlines()

    # Iterujemy przez każdą nazwę pliku
    for file_name in file_names:
        # Sprawdzamy, czy rozszerzenie pliku ma dokładnie 4 znaki (po kropce)
        if len(file_name.split('.')[-1]) == 4:
            # Drukujemy nazwę pliku, jeśli spełnia warunek
            print(file_name)
