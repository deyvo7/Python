from e_book import EBook  # Importujemy klasę EBook z pliku e_book.py

def main():
    # Tworzymy książkę
    my_book = EBook("Wielki Gatsby", "F. Scott Fitzgerald", 180)
    
    # Otwarcie książki
    print("Otwieramy książkę...")
    my_book.open_book()
    my_book.display_status()  # Wyświetlamy status książki

    # Czytamy kilka stron
    print("\nCzytamy kilka stron...")
    my_book.read_next_page()
    my_book.read_next_page()
    my_book.display_status()  # Wyświetlamy status książki po zmianie stron

    # Zamykanie książki
    print("\nZamykamy książkę...")
    my_book.close_book()
    my_book.display_status()  # Wyświetlamy status książki po zamknięciu
    
    # Próba czytania po zamknięciu książki
    print("\nPróba czytania po zamknięciu książki...")
    my_book.read_next_page()

if __name__ == "__main__":
    main()  # Uruchamiamy główną funkcję programu
