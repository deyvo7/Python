from bank_account import BankAccount  # Importujemy klasę BankAccount

def main():
    """
    Główna funkcja programu. Tworzy konto bankowe i wykonuje operacje na koncie:
    - Wyświetla saldo konta.
    - Wpłaca środki na konto.
    - Próbuje wypłacić więcej niż dostępne środki.
    - Wypłaca dostępną kwotę i wyświetla końcowe saldo.
    """
    # Tworzymy obiekt reprezentujący konto bankowe z podanym numerem
    account = BankAccount("12 3456 5555 9090 1111 0000 7722")
    
    # Wyświetlamy początkowe informacje o koncie
    print("Początkowy stan konta:")
    account.display_account_info()
    
    # Wpłacamy środki na konto
    print("\nWpłata środków:")
    account.deposit(25.30)  # Wpłacamy 25,30 PLN
    account.display_account_info()  # Wyświetlamy saldo po wpłacie
    
    # Próba wypłacenia większej kwoty niż dostępna
    print("\nPróba wypłaty większej kwoty niż saldo:")
    account.withdraw(31.70)  # Próba wypłaty 31,70 PLN
    account.display_account_info()  # Wyświetlamy saldo po nieudanej próbie wypłaty
    
    # Wypłata dostępnych środków
    print("\nWypłata dostępnej kwoty:")
    account.withdraw(14.00)  # Wypłacamy 14,00 PLN
    account.display_account_info()  # Wyświetlamy końcowe saldo

if __name__ == "__main__":
    # Uruchamiamy główną funkcję programu
    main()
