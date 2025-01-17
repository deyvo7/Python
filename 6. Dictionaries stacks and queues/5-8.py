# Cennik produktów (słownik)
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Koszyk zakupowy (słownik), gdzie kluczem jest nazwa produktu, a wartością ilość
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Zmienna, która będzie przechowywać całkowity koszt zakupów
total_cost = 0

# Iterujemy przez koszyk zakupowy (zawiera produkty i ich ilości)
for item, quantity in cart.items():
    # Sprawdzamy, czy dany produkt znajduje się w cenniku
    if item in prices:
        # Obliczamy koszt tego produktu (ilość * cena jednostkowa) i dodajemy do całkowitego kosztu
        total_cost += prices[item] * quantity

# Wypisujemy całkowity koszt zakupów, zaokrąglony do dwóch miejsc po przecinku
print(f"Całkowity koszt zakupów: ${total_cost:.2f}")
