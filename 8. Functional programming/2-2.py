# Definiujemy listę imion, która będzie posortowana według długości (liczby liter) imion
names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

# Używamy funkcji sorted() do posortowania listy.
# Funkcja sorted() przyjmuje dwa argumenty:
# - pierwszym argumentem jest lista, którą chcemy posortować
# - drugim argumentem jest key, który może być funkcją służącą do określenia, po jakim kluczu mamy sortować.
# W tym przypadku używamy funkcji lambda, która zwraca długość imienia (liczbę liter) jako klucz sortowania.
names_sorted = sorted(names, key=lambda name: len(name))

# Wypisujemy posortowaną listę
print(names_sorted)
