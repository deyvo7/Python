# Definiujemy listę pracowników w postaci ciągów tekstowych, gdzie imię i nazwisko są rozdzielone spacją.
employees = ["SMITH Lucy", "JONES Janet", "LEE Jerry",
             "JACKSON Peter", "JOHNSON Rick",
             "LEWIS Terry", "CLARKE Robin"]

# Używamy funkcji filter() z funkcją anonimową (lambda), aby wybrać pracowników, 
# których nazwisko zaczyna się na literę 'J'.
# Funkcja lambda sprawdza pierwszą literę nazwiska (zaczynamy od 0 indeksu, po spacjach)
emp_J = list(filter(lambda e: e.split()[0][0] == "J", employees))

# Wypisujemy wynik - listę pracowników, których nazwiska zaczynają się na 'J'
print(emp_J)
