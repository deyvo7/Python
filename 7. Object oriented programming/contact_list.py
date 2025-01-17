# Plik contact_list.py
from contact import Contact

class ContactList:
    """
    Klasa ContactList przechowuje listę kontaktów.
    Umożliwia dodawanie nowych kontaktów oraz wyświetlanie całej listy kontaktów.
    """

    def __init__(self):
        # Tworzymy pustą listę na kontakty
        self.contacts = []

    def add_contact(self, contact):
        """
        Dodaje nowy kontakt do listy.
        - contact: Obiekt klasy Contact, który ma być dodany.
        """
        self.contacts.append(contact)

    def display_contacts(self):
        """
        Wyświetla listę kontaktów w czytelnej formie.
        """
        print("Lista kontaktów na smartfonie:")
        print("Imię i nazwisko\tE-mail\t\t\tNumer telefonu")
        print("-" * 50)  # Separator
        for contact in self.contacts:
            print(contact)  # Wywołanie metody __str__ z klasy Contact
