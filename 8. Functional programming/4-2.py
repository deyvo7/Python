# Definiujemy listę zarejestrowanych prędkości pojazdów.
values = [48, 47, 54, 50, 42, 68, 39, 46]

# Używamy funkcji filter() z funkcją anonimową (lambda), aby znaleźć prędkości, które są wyższe niż dozwolone 50 km/h.
# Funkcja lambda sprawdza, czy wartość w liście jest większa niż 50.
too_high = list(filter(lambda x: x > 50, values))

# Wypisujemy wyniki:
# - Zarejestrowane prędkości
# - Prędkości, które przekroczyły dozwoloną wartość
print("Recorded values: ", values)
print("Speed too high: ", too_high)
