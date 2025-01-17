import json

# Tworzymy pusty słownik, w którym będziemy przechowywać dane o produkcie
product = {}

# Pobieramy dane od użytkownika o produkcie
product['name'] = input("Podaj nazwę produktu: ")  # Nazwa produktu, dane tekstowe (string)

# Pobieramy cenę produktu jako liczbę zmiennoprzecinkową z dwoma miejscami po przecinku
product['price'] = float(input("Podaj cenę produktu: "))  # Cena produktu, liczba zmiennoprzecinkowa (float)

# Pobieramy informację, czy produkt został opłacony (tak/nie) i zamieniamy to na wartość logiczną (True/False)
paid_input = input("Czy produkt został opłacony? (tak/nie): ").strip().lower()  # Pobieramy odpowiedź użytkownika
if paid_input == 'tak':  # Jeśli odpowiedź to 'tak', ustawiamy wartość na True
    product['paid'] = True
elif paid_input == 'nie':  # Jeśli odpowiedź to 'nie', ustawiamy wartość na False
    product['paid'] = False
else:
    print("Niepoprawna odpowiedź, ustawiamy domyślnie jako nieopłacony.")
    product['paid'] = False  # Domyślna wartość, jeśli użytkownik poda coś innego niż 'tak' lub 'nie'

# Określamy nazwę pliku, w którym zapiszemy dane o produkcie
file_name = "product.json"

# Otwieramy plik w trybie zapisu i zapisujemy dane w formacie JSON
with open(file_name, 'w') as file:
    json.dump(product, file, indent=4)  # Zapisujemy dane do pliku JSON z wcięciami dla czytelności

# Wyświetlamy informację o zapisaniu danych
print("Dane o produkcie zostały zapisane do pliku", file_name)
