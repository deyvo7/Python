class EBook:
    def __init__(self, title, author, num_pages):
        """
        Konstruktor inicjujący książkę elektroniczną z tytułem, autorem
        i liczbą stron.
        """
        self.title = title  # Tytuł książki
        self.author = author  # Autor książki
        self.num_pages = num_pages  # Liczba stron książki
        self.current_page = 1  # Strona, na której się aktualnie znajdujemy
        self.is_open = False  # Książka jest początkowo zamknięta

    def open_book(self):
        """Otwiera książkę."""
        self.is_open = True
        self.current_page = 1  # Po otwarciu książki zaczynamy od pierwszej strony

    def close_book(self):
        """Zamyka książkę."""
        self.is_open = False

    def read_next_page(self):
        """Przechodzi do następnej strony, jeśli książka jest otwarta."""
        if self.is_open:
            if self.current_page < self.num_pages:
                self.current_page += 1  # Przechodzimy do następnej strony
            else:
                print("Jesteś już na ostatniej stronie książki.")
        else:
            print("Książka jest zamknięta. Otwórz ją, aby czytać.")

    def read_previous_page(self):
        """Przechodzi do poprzedniej strony, jeśli książka jest otwarta."""
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1  # Przechodzimy do poprzedniej strony
            else:
                print("Jesteś już na pierwszej stronie książki.")
        else:
            print("Książka jest zamknięta. Otwórz ją, aby czytać.")

    def display_status(self):
        """Wyświetla status książki: tytuł, autor, liczba stron i aktualna strona."""
        if self.is_open:
            print(f"Książka: {self.title} autorstwa {self.author}")
            print(f"Liczba stron: {self.num_pages}, Aktualna strona: {self.current_page}")
        else:
            print(f"Książka: {self.title} autorstwa {self.author} jest zamknięta.")
