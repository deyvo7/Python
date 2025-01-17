import json

# Otwórz plik JSON w trybie do odczytu
with open('computer.json', 'r', encoding='utf-8') as file:
    # Załaduj dane z pliku JSON do zmiennej
    data = json.load(file)

# Wypisz dane komputera
for key, value in data.items():
    print(f"{key}: {value}")
