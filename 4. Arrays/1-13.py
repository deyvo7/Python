# The store has 10 types of goods in stock.
# The prices of the goods and the number of pieces of goods
# are given below. Write a program that calculates the value of
# all the goods available in the store.

# Ceny produktów w sklepie komputerowym (w jednostkach walutowych)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Ilość dostępnych jednostek dla każdego produktu
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# Zmienna do przechowywania całkowitej wartości produktów
total_value = 0

# Iterujemy przez każdy produkt
for index in range(len(product_quantities)):
    # Mnożymy cenę produktu przez jego ilość i dodajemy do całkowitej wartości
    total_value += product_prices[index] * product_quantities[index]

# Wypisujemy całkowitą wartość produktów w sklepie
print("Total value of all goods in the store:", total_value)
