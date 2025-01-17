# Write a program that counts the number of occurrences of any value from a tuple. Sample result:

# Tuple: 50,20,40,50,30,50
# Value: 50
# Number of occurrences: 3

# Definiujemy krotkę z liczbami
my_tuple = (50, 20, 40, 50, 30, 50)

# Określamy wartość, której wystąpienia chcemy policzyć
value_to_count = 50

# Używamy metody count() do policzenia wystąpień wartości w krotce
occurrences = my_tuple.count(value_to_count)

# Wyświetlamy wynik
print("Tuple:", my_tuple)
print("Value:", value_to_count)
print("Number of occurrences:", occurrences)
