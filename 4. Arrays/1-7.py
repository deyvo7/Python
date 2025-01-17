# Write a program that prints a shopping list,
# each product on a separate line.

###
# Prints shopping list
#
# Wypisuje listę zakupów
# Tworzymy listę zakupów z produktami
shopping_list = [
    "milk", "bread", "eggs", "butter", "cheese",
    "tomatoes", "potatoes", "carrots", "onions", "garlic"
]

# Używamy pętli for, aby wypisać każdy produkt w osobnym wierszu
for item in shopping_list:  # Iterujemy przez elementy listy
    print(item)  # Wypisujemy bieżący element
