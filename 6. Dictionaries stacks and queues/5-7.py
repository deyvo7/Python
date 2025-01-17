# Funkcja zwracająca listę nazw hoteli, połączonych przecinkami
def hotel_list(hotels):
    # Iterujemy przez listę hoteli i zwracamy ich nazwy połączone przecinkami
    return ", ".join([hotel["name"] for hotel in hotels])

# Funkcja obliczająca średnią cenę za pokój w hotelach
def avg_price(hotels):
    # Sumujemy ceny pokoi w hotelach
    total_price = sum(hotel["price"] for hotel in hotels)
    # Obliczamy średnią cenę, dzieląc sumę przez liczbę hoteli i zaokrąglamy wynik
    return round(total_price / len(hotels))

# Lista hoteli w Krakowie z nazwą i ceną za pokój
hotels_in_Krakow = [
   {"name": "Sky", "price": 320.00},      # Hotel Sky, cena 320 zł
   {"name": "Metropol", "price": 480.00},  # Hotel Metropol, cena 480 zł
   {"name": "New Port", "price": 420.00},  # Hotel New Port, cena 420 zł
   {"name": "Aparthotel", "price": 390.00} # Hotel Aparthotel, cena 390 zł
]

# Lista hoteli w Sopocie z nazwą i ceną za pokój
hotels_in_Sopot = [
   {"name": "Focus", "price": 510.00},        # Hotel Focus, cena 510 zł
   {"name": "Aqua", "price": 345.00},         # Hotel Aqua, cena 345 zł
   {"name": "La Boutique", "price": 390.00},  # Hotel La Boutique, cena 390 zł
   {"name": "Marina", "price": 410.00}        # Hotel Marina, cena 410 zł
]

# Wyświetlanie listy hoteli i obliczenie średniej ceny w Krakowie
print(f"Hotels in Krakow: {hotel_list(hotels_in_Krakow)}")  # Wypisuje nazwy hoteli w Krakowie
avg_krakow = avg_price(hotels_in_Krakow)  # Oblicza średnią cenę w Krakowie
print(f"Average hotel price in Krakow: {avg_krakow}")  # Wypisuje średnią cenę w Krakowie

# Wyświetlanie listy hoteli i obliczenie średniej ceny w Sopocie
print(f"Hotels in Sopot: {hotel_list(hotels_in_Sopot)}")  # Wypisuje nazwy hoteli w Sopocie
avg_sopot = avg_price(hotels_in_Sopot)  # Oblicza średnią cenę w Sopocie
print(f"Average hotel price in Sopot: {avg_sopot}")  # Wypisuje średnią cenę w Sopocie

# Porównanie, w którym mieście hotele są tańsze
# Jeśli średnia cena w Krakowie jest mniejsza niż w Sopocie, hotele w Krakowie są tańsze
cheaper_in = "Krakow" if avg_krakow < avg_sopot else "Sopot"
print(f"Cheaper hotels in: {cheaper_in}")  # Wypisuje miasto z tańszymi hotelami
