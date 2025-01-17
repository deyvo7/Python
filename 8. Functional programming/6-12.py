# Lista danych o medalach zdobytych przez kraje
medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},  # Dania - 2 złote, 4 srebrne, 6 brązowych
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},  # Finlandia - 5 złotych, 0 srebrnych, 4 brązowe
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},    # USA - 12 złotych, 5 srebrnych, 11 brązowych
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}      # Peru - 0 złotych, 1 srebrne, 7 brązowych
]

# Używamy funkcji filter() i lambda, aby wybrać tylko te kraje, które zdobyły co najmniej 10 medali
# Suma medali to suma złotych, srebrnych i brązowych
countries_with_10_or_more_medals = list(filter(lambda country: (country["gold"] + country["silver"] + country["bronze"]) >= 10, medals))

# Wyświetlamy nagłówek
print("COUNTRIES WITH AT LEAST 10 MEDALS")

# Dla każdego kraju w przefiltrowanej liście, wypisujemy nazwę kraju oraz liczbę zdobytych medali
for country in countries_with_10_or_more_medals:
    print(f"{country['country']}: {country['gold']},{country['silver']},{country['bronze']}")
