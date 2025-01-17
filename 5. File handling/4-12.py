# The file books.csv contains a list of books. Write a program that copies the book data from a given genre to its 
# corresponding file. Use functions to divide the program into logical parts.

# Genre --> Filename
# Fantasy --> books_fantasy.txt
# Historical --> books_historical.txt
# Romance --> books_romance.txt
# Classic --> books_classic.txt  

import csv

# Funkcja do odczytania książek z pliku CSV
def read_books(file_name):
    books = []  # Lista na książki
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Używamy DictReader do wczytania wierszy jako słowników
        for row in reader:
            books.append(row)  # Dodajemy każdą książkę do listy
    return books

# Funkcja do zapisywania książek do odpowiedniego pliku na podstawie gatunku
def write_books_by_genre(genre, books):
    # Mapowanie gatunków na nazwy plików
    genre_to_filename = {
        'Fiction': 'books_fiction.txt',
        'Dystopian': 'books_dystopian.txt',
        'Classic': 'books_classic.txt',
        'Romance': 'books_romance.txt',
        'Adventure': 'books_adventure.txt',
        'Historical': 'books_historical.txt',
        'Modernist': 'books_modernist.txt',
        'Epic': 'books_epic.txt',
        'Gothic': 'books_gothic.txt',
        'Psychological': 'books_psychological.txt',
        'Fantasy': 'books_fantasy.txt',
        'Philosophical': 'books_philosophical.txt',
        'Literary': 'books_literary.txt',
        'Southern Gothic': 'books_southern_gothic.txt',
        'Magic Realism': 'books_magic_realism.txt',
        'Gothic Horror': 'books_gothic_horror.txt',
        'Novella': 'books_novella.txt',
        'Science Fiction': 'books_science_fiction.txt',
        'Satire': 'books_satire.txt',
        'Post-apocalyptic': 'books_post_apocalyptic.txt',
        'Horror': 'books_horror.txt'
    }

    # Sprawdzamy, czy gatunek jest w słowniku
    if genre not in genre_to_filename:
        print(f"Nieobsługiwany gatunek: {genre}")
        return

    # Zapisujemy książki do pliku, jeśli gatunek pasuje
    with open(genre_to_filename[genre], 'w', encoding='utf-8') as file:
        for book in books:
            if book['Genre'] == genre:
                # Zapisujemy książkę w formacie: Title, Author, Genre, Year
                file.write(f"{book['Title']},{book['Author']},{book['Genre']},{book['Year']}\n")
        print(f"Książki z gatunku {genre} zostały zapisane do pliku {genre_to_filename[genre]}")

# Funkcja główna
def main():
    # Odczytujemy książki z pliku CSV
    books = read_books('books.csv')

    # Lista gatunków, dla których zapisujemy książki
    genres = ['Fiction', 'Dystopian', 'Classic', 'Romance', 'Adventure', 'Historical', 
              'Modernist', 'Epic', 'Gothic', 'Psychological', 'Fantasy', 'Philosophical', 
              'Literary', 'Southern Gothic', 'Magic Realism', 'Gothic Horror', 'Novella', 
              'Science Fiction', 'Satire', 'Post-apocalyptic', 'Horror']

    # Dla każdego gatunku wywołujemy funkcję zapisującą książki
    for genre in genres:
        write_books_by_genre(genre, books)

# Uruchamiamy główną funkcję
if __name__ == "__main__":
    main()
