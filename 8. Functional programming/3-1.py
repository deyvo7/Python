# Definiujemy listę transakcji w Euro
transactions_in_eur = [15.90, 38.47, 4.07, 132.70, 9.15]

# Używamy funkcji map() z funkcją anonimową (lambda), aby przeliczyć wszystkie transakcje z Euro na złote.
# Każdą wartość w liście (transakcję) mnożymy przez 4.5, aby przeliczyć na złote.
# Funkcja map() zwraca mapę, więc musimy użyć list() aby przekonwertować wynik na listę.
transactions_in_pln = list(map(lambda x: x * 4.5, transactions_in_eur))

# Wypisujemy wynik (transakcje w złotych)
print(transactions_in_pln)
