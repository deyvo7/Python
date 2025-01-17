import json

# Wczytaj dane z pliku JSON (jeśli istnieje), jeśli nie, zacznij od pustego słownika
try:
    with open('voting.json', 'r') as file:
        voting_data = json.load(file)
except FileNotFoundError:
    voting_data = {}

# Zapytaj użytkownika o nazwisko osoby, na którą głosuje
person_name = input('Podaj nazwisko osoby, na którą głosujesz: ')

# Zwiększ liczbę głosów dla podanej osoby (lub dodaj ją, jeśli nie istnieje w słowniku)
if person_name in voting_data:
    voting_data[person_name] += 1  # Zwiększ głos o 1
else:
    voting_data[person_name] = 1  # Dodaj osobę z jednym głosem

# Zapisz zaktualizowane dane do pliku JSON
with open('voting.json', 'w') as file:
    json.dump(voting_data, file, indent=4)

print(f"Głos na {person_name} został dodany!")
