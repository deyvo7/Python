# Tworzymy słownik (dictionary) przechowujący listę produktów wraz z ich cenami w sklepie odzieżowym.
price_list = {
    'T-shirt': 19.99,   # Koszulka: 19.99 zł
    'Jeans': 49.99,     # Dżinsy: 49.99 zł
    'Jacket': 89.99,    # Kurtka: 89.99 zł
    'Sneakers': 59.99,  # Buty sportowe: 59.99 zł
    'Hat': 15.99        # Czapka: 15.99 zł
}

# Wyświetlamy ceny produktów przed rabatem.
print("Ceny przed rabatem:")
for key, value in price_list.items():
    print(f"{key}: {value:.2f} zł")  # Formatowanie ceny z dokładnością do 2 miejsc po przecinku.

# Obliczamy całkowitą wartość produktów przed rabatem.
total = 0  # Zmienna do przechowywania sumy cen.
for key, value in price_list.items():
    total += value  # Dodajemy cenę każdego produktu do zmiennej 'total'.
total = round(total, 2)  # Zaokrąglamy sumę do 2 miejsc po przecinku.
print(f"Całkowita wartość produktów przed rabatem: {total:.2f} zł")

# Wyświetlamy ceny produktów po obniżce 10% i aktualizujemy słownik.
print("Ceny po rabacie:")
for key, value in price_list.items():
    new_value = round(value * 0.9, 2)  # Obliczamy nową cenę, zmniejszając ją o 10%, i zaokrąglamy do 2 miejsc po przecinku.
    price_list[key] = new_value  # Aktualizujemy cenę produktu w słowniku.
    print(f"{key}: {new_value:.2f} zł")

# Obliczamy całkowitą wartość produktów po rabacie.
total = 0  # Resetujemy zmienną 'total'.
for key, value in price_list.items():
    total += value  # Dodajemy nową cenę każdego produktu do zmiennej 'total'.
total = round(total, 2)  # Zaokrąglamy sumę do 2 miejsc po przecinku.
print(f"Całkowita wartość produktów po rabacie: {total:.2f} zł")
