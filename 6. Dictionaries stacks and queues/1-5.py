# Tworzymy listę (array) zawierającą 5 słowników (dictionaries).
# Każdy słownik reprezentuje kraj i jego populację.
countries = [
    {"country": "Poland", "population": 38000000},      # Polska z populacją 38 milionów
    {"country": "Turkey", "population": 55645000},     # Turcja z populacją 55,645 milionów
    {"country": "Thailand", "population": 2140000},    # Tajlandia z populacją 2,14 milionów
    {"country": "Slovakia", "population": 2455000},    # Słowacja z populacją 2,455 milionów
    {"country": "Germany", "population": 50000000}     # Niemcy z populacją 50 milionów
]

# Wyświetlamy nagłówek tabeli.
# Pierwsza kolumna to "COUNTRY" (nazwa kraju), druga to "POPULATION" (populacja kraju).
print("COUNTRY      POPULATION")

# Iterujemy przez każdy słownik w liście "countries".
for dict in countries:
    # Wyświetlamy nazwę kraju (wartość klucza "country") oraz jego populację (wartość klucza "population").
    # Używamy F-stringów, aby sformatować dane w czytelny sposób.
    print(f"{dict['country']}       {dict['population']}")
