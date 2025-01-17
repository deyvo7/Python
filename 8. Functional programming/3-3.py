# Definiujemy dane: lista produktów w magazynie i ich cena za sztukę
stock = [(20, 5.50), (15, 8.30), (37, 3.85), (4, 11.60)]

# Używamy funkcji map(), aby obliczyć wartość każdego produktu w magazynie.
# Funkcja lambda mnoży liczbę sztuk (item[0]) przez cenę jednostkową (item[1]).
# Funkcja map() stosuje lambda do każdego elementu w liście "stock" i zwraca wynik.
value = list(map(lambda item: item[0] * item[1], stock))

# Używamy funkcji sum() do obliczenia łącznej wartości wszystkich produktów w magazynie.
total_value = sum(value)

# Wypisujemy dane i wynik
print("Products in stock: ", stock)
print("Total value: ", total_value)
