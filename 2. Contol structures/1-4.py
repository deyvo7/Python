###
# Credit card payment 
#
###
# Płatność kartą kredytową
###

# Ustawienie salda konta
account_balance = 500

# Wczytanie całkowitej kwoty płatności od użytkownika
total_payment = int(input("Enter the total payment: "))

# Sprawdzenie, czy kwota płatności nie przekracza salda konta
if total_payment <= account_balance:
    # Jeśli kwota płatności jest mniejsza lub równa saldu, wyświetl komunikat o zakończeniu płatności
    print('Payment completed')
else:
    # Jeśli kwota płatności przekracza saldo, wyświetl komunikat o braku środków
    print('No funds')
