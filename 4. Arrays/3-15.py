# Write a program that prints the tuple (10,20,30,40,50) in reverse order. Sample result:

# Tuple: 10,20,30,40,50
# Reverse order: 50,40,30,20,10

# Definiujemy krotkę
my_tuple = (10, 20, 30, 40, 50)

# Drukujemy oryginalną krotkę
print("Tuple:", my_tuple)

# Drukujemy krotkę w odwrotnej kolejności
print("Reverse order:", my_tuple[::-1])


# W Pythonie do odwracania krotek możemy użyć techniki tzw. "slicing" (krojenie) z użyciem [::-1], co oznacza,
# że bierzemy całą krotkę i przesuwamy ją wstecz, czyli odwracamy kolejność elementów.
# [::-1] oznacza:
# : - bierzemy całą krotkę.
# -1 - krok co -1, czyli wstecz (odwrócenie).