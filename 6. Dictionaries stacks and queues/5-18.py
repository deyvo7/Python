import json

# Otwórz plik JSON w trybie do odczytu
with open('dogs.json', 'r', encoding='utf-8') as file:
    # Załaduj dane z pliku JSON do zmiennej
    dogs = json.load(file)

# Iterujemy po liście psów
for dog in dogs:
    # Jeśli wiek psa jest mniejszy niż 5
    if dog['age'] < 5:
        # Wypisz dane o psie
        print(f"Name: {dog['name']}")
        print(f"Breed: {dog['breed']}")
        print(f"Age: {dog['age']}")
        print(f"Weight: {dog['weight_kg']} kg")
        print(f"Owner: {dog['owner']}")
        print(f"Vaccinated: {'Yes' if dog['vaccinated'] else 'No'}")
        print()  # Pusta linia między psami
