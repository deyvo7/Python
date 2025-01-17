# Write a program that calculates the number of lines, characters and words for any text file.
# The user enters the name of the file from the keyboard. Use a try-except block to avoid interrupting your program
# when the user enters a filename that doesn't exist. Print the result of the calculation.
# To check if the program is working correctly, find 3 text files on the Internet and use them to test the program.

# Sample result:
# File name: books.txt
# Number of lines: 14
# Number of characters: 2540
# Number of words: 703

# Funkcja do liczenia właściwości pliku (liczba linii, znaków, słów)
def count_file_properties(file_name):
    try:
        # Zmienna do liczenia liczby linii
        lines_count = 0
        # Zmienna do liczenia liczby znaków (w tym spacji)
        characters_count = 0
        # Zmienna do liczenia liczby słów
        words_count = 0
        
        # Otwarcie pliku w trybie do odczytu ('r') z kodowaniem UTF-8
        with open(file_name, 'r', encoding='utf-8') as file:
            # Przechodzimy przez plik linia po linii
            for line in file:
                # Zwiększamy licznik linii o 1 za każdą przeczytaną linię
                lines_count += 1
                # Zliczamy liczbę znaków (w tym spacji) w danej linii
                characters_count += len(line)
                # Rozdzielamy linię na słowa (domyślnie po białych znakach) i liczymy liczbę słów
                words_count += len(line.split())

        # Zwracamy liczbę linii, znaków i słów jako krotkę
        return lines_count, characters_count, words_count
    except FileNotFoundError:
        # Jeśli plik nie istnieje, wyświetlamy komunikat o błędzie
        print(f"Error: Plik '{file_name}' nie istnieje.")
        return None, None, None  # Zwracamy None w przypadku błędu

# Pobieramy nazwę pliku od użytkownika
file_name = input("Wprowadź nazwę pliku: ")

# Wywołujemy funkcję, aby obliczyć liczbę linii, znaków i słów w pliku
lines, characters, words = count_file_properties(file_name)

# Jeśli plik został znaleziony i dane zostały obliczone, wyświetlamy wyniki
if lines is not None:
    print(f"Nazwa pliku: {file_name}")
    print(f"Liczba linii: {lines}")  # Liczba linii w pliku
    print(f"Liczba znaków: {characters}")  # Liczba znaków w pliku (w tym spacje)
    print(f"Liczba słów: {words}")  # Liczba słów w pliku
