# A computer program analyses the price of a product in an online store.
# If the product price decreases by at least 10%, the program prints a purchase recommendation:

# Buy the product!!
# Product price reduced by 17%
# Create such program. The current and previous price of the product are included in variables. Sample result:

# Current product price: 140.00
# Previous product price: 200.00
# Buy the product!!
# Product price reduced by 30%

###
# Program analizujący cenę produktu w sklepie internetowym
# Jeśli cena produktu spadła o co najmniej 10%, program wyświetli rekomendację zakupu.
###

# Pobranie bieżącej ceny produktu od użytkownika
current_price = float(input("Enter the current price: "))

# Pobranie poprzedniej ceny produktu od użytkownika
previous_price = float(input("Enter the previous price: "))

# Obliczenie procentowej obniżki ceny
reduction = ((previous_price - current_price) / previous_price) * 100

# Wyświetlenie bieżącej i poprzedniej ceny
print(f"Current product price: {current_price}")
print(f"Previous product price: {previous_price}")

# Sprawdzenie, czy cena spadła o co najmniej 10%
if current_price < previous_price and reduction >= 10:
    # Jeśli cena spadła o 10% lub więcej, rekomendacja zakupu
    print("Buy the product!!")
    print(f"Product price reduced by {reduction}%")
else:
    # Jeśli cena nie spadła o co najmniej 10%, nie zaleca się zakupu
    print("Don't buy it.")
