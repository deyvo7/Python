# In one of the online stores, a 25% discount is charged for each product purchased over two. 
# Write a program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard.
# Sample result:

# Number of products purchased: 5
# Product price: 40
# Amount to pay: 170.00

import math

# Pobranie danych od użytkownika
purchased_products = int(input("Enter the number of products purchased: "))
product_price = float(input("Enter the price of the products: "))

# Obliczanie ceny do zapłaty
if purchased_products > 2:
    # Jeżeli zakupiono więcej niż 2 produkty, dla połowy z nich zastosujemy rabat
    discounted_products = math.floor(purchased_products / 2)  # Zastosowanie rabatu do połowy produktów
    amount_to_pay = (purchased_products - discounted_products) * product_price + discounted_products * product_price * 0.75
else:
    # Jeśli zakupiono 2 lub mniej produktów, nie ma rabatu
    amount_to_pay = purchased_products * product_price

# Wyświetlenie wyniku
print("Number of products purchased:", purchased_products)
print("Product price:", product_price)
print(f"Amount to pay: {amount_to_pay:.2f}")
