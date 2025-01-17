import json

# Otwórz plik JSON w trybie do odczytu
with open('cities.json', 'r', encoding='utf-8') as file:
    # Załaduj dane z pliku JSON do zmiennej
    data = json.load(file)

# Wypisz dane o miastach
for city in data:
    for key, value in city.items():
        print(key, ':', value)
    print()  # Pusta linia między miastami dla lepszej czytelności
