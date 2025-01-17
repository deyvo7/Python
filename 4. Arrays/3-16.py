# Write a program that for the tuple ("Seven", [10, 20, 30], (5, 15, 25)) prints values:

# “Seven”
# 30

# Definiujemy krotkę z różnymi typami danych
my_tuple = ("Seven", [10, 20, 30], (5, 15, 25))

# Drukujemy pierwszy element krotki, czyli string "Seven"
print(my_tuple[0])

# Drukujemy ostatni element listy (drugi element krotki), czyli 30
print(my_tuple[1][-1])

# my_tuple[1][-1] oznacza ostatni element tej listy, ponieważ indeks -1 w Pythonie odnosi się do ostatniego elementu.