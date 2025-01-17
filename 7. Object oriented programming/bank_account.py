class BankAccount:
    def __init__(self, account_number):
        """
        Konstruktor klasy BankAccount. Inicjalizuje konto bankowe z podanym numerem konta
        oraz ustawia początkowe saldo na 0.0 PLN.
        
        :param account_number: Numer konta bankowego w formacie string (26 cyfr)
        """
        self.account_number = account_number  # Przypisujemy numer konta
        self.balance = 0.0  # Ustawiamy początkowe saldo na 0.0 PLN

    def deposit(self, amount):
        """
        Metoda do wpłacania środków na konto. Dodaje określoną kwotę do obecnego salda.
        
        :param amount: Kwota do wpłacenia (float) - musi być większa od 0
        """
        if amount > 0:  # Sprawdzamy, czy kwota jest dodatnia
            self.balance += amount  # Dodajemy kwotę do salda
            print(f"PLN {amount:.2f} deposited.")  # Informujemy użytkownika o wpłacie
        else:
            print("Deposit amount must be greater than zero.")  # Błąd, jeśli kwota <= 0

    def withdraw(self, amount):
        """
        Metoda do wypłacania środków z konta. Odejmuje określoną kwotę od salda,
        o ile saldo jest wystarczające.
        
        :param amount: Kwota do wypłacenia (float)
        """
        if amount <= self.balance:  # Sprawdzamy, czy wystarczające środki są dostępne
            self.balance -= amount  # Odejmuje kwotę od salda
            print(f"PLN {amount:.2f} withdrawn.")  # Informujemy użytkownika o wypłacie
        else:
            print("Insufficient funds on the account.")  # Komunikat o braku środków

    def display_account_info(self):
        """
        Metoda do wyświetlania informacji o numerze konta i jego aktualnym saldzie.
        """
        print(f"Bank Account No: {self.account_number}")  # Wyświetlamy numer konta
        print(f"Balance: PLN {self.balance:.2f}")  # Wyświetlamy saldo konta
