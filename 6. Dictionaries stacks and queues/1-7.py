# Tworzymy słownik (dictionary), który przechowuje informacje o produktach i ich ilości w sklepie.
# Klucze to nazwy produktów, a wartości to ilości dostępnych sztuk.
products = {
    'Laptop': 15,                    # Laptop: 15 sztuk
    'Desktop PC': 10,                # Komputer stacjonarny: 10 sztuk
    'Monitor': 25,                   # Monitor: 25 sztuk
    'Keyboard': 50,                  # Klawiatura: 50 sztuk
    'Mouse': 60,                     # Mysz: 60 sztuk
    'External Hard Drive': 30,       # Zewnętrzny dysk twardy: 30 sztuk
    'Printer': 12,                   # Drukarka: 12 sztuk
    'Router': 20,                    # Router: 20 sztuk
    'USB Flash Drive': 100,          # Pamięć USB: 100 sztuk
    'Graphics Card': 8               # Karta graficzna: 8 sztuk
}

# Iterujemy przez wszystkie produkty w słowniku i wyświetlamy ich nazwy oraz ilości.
print("Lista produktów i ilości:")
for key, value in products.items():
    print(f"{key}: {value}")  # Wyświetlamy nazwę produktu i odpowiadającą mu ilość.

# Obliczamy całkowitą liczbę produktów w sklepie.
# Tworzymy zmienną 'total' i ustawiamy jej początkową wartość na 0.
total = 0
for key, value in products.items():
    total += value  # Dodajemy ilość każdego produktu do zmiennej 'total'.

# Wyświetlamy całkowitą liczbę produktów.
print(f"Całkowita liczba produktów w sklepie: {total}")
