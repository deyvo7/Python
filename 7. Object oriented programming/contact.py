# Plik contact.py
class Contact:
    """
    Klasa Contact opisuje pojedynczy kontakt.
    Zawiera pola:
    - name: Imię i nazwisko kontaktu
    - email: Adres e-mail kontaktu
    - telephone: Numer telefonu kontaktu
    """

    def __init__(self, name, email, telephone):
        # Inicjalizacja obiektu Contact z danymi kontaktu
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        """
        Funkcja zwracająca czytelną reprezentację kontaktu w formie tekstowej.
        """
        return f"{self.name}\t{self.email}\t{self.telephone}"
