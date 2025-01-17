import json

# Otwieramy plik euro.json w trybie odczytu
with open('euro.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Nagłówek tabeli
print(f"{'Date':<15}{'Buying Rate':<15}{'Selling Rate':<15}")
print("="*45)

# Iterujemy przez dane i wyświetlamy kursy
for rate in data['rates']:
    date = rate['effectiveDate']
    buying_rate = rate['bid']
    selling_rate = rate['ask']
    print(f"{date:<15}{buying_rate:<15}{selling_rate:<15}")
