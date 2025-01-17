# Definicja klasy Book, reprezentującej książkę
class Book():
    # Konstruktor klasy, który ustawia początkowe wartości dla tytułu, autora, liczby stron i ceny książki
    def __init__(self, title, author, pages, price):
        self.title = title        # Tytuł książki
        self.author = author      # Autor książki
        self.pages = pages        # Liczba stron w książce
        self.current_page = 1     # Początkowa strona to 1
        self.is_open = False      # Książka początkowo jest zamknięta
        self.price = price        # Cena książki

    # Metoda otwierająca książkę
    def open(self):
        self.is_open = True
    
    # Metoda zamykająca książkę
    def close(self):
        self.is_open = False
    
    # Metoda zmieniająca stronę książki na wskazaną
    def change_page(self, page):
        self.current_page = page

    # Metoda wyświetlająca informacje o książce
    def display_info(self):
        print(f"Moja ulubiona książka to {self.title}.")
        print(f"Napisał ją {self.author}.")
        print(f"Książka ma {self.pages} stron.")
        print(f"Cena książki to {self.price} zł.")
        if self.is_open:
            print(f"Obecnie czytam książkę, strona {self.current_page}.")
        else:
            print("Zamierzam przeczytać książkę później.")

# Funkcja główna, która tworzy obiekt książki i wywołuje odpowiednie metody
def main():
    # Tworzenie obiektu książki na podstawie klasy Book
    favourite_book = Book(
        "Harry Potter i Kamień Filozoficzny",
        "J. K. Rowling", 223, 48)

    # Manipulacja obiektem
    favourite_book.open()                  # Otwórz książkę
    favourite_book.change_page(15)         # Zmień stronę na 15
    favourite_book.display_info()          # Wyświetl informacje o książce
    favourite_book.close()                 # Zamknij książkę

# Sprawdzenie, czy kod jest uruchamiany jako główny skrypt
if __name__ =="__main__":
    main()
