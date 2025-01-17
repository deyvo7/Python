import matplotlib.pyplot as plt

# Lista danych o medalach zdobytych przez kraje
medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},  # Dania - 2 złote, 4 srebrne, 6 brązowych
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},  # Finlandia - 5 złotych, 0 srebrnych, 4 brązowe
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},    # USA - 12 złotych, 5 srebrnych, 11 brązowych
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}      # Peru - 0 złotych, 1 srebrne, 7 brązowych
]

# 1. Używamy funkcji map(), aby obliczyć całkowitą liczbę medali dla każdego kraju
total_medals = list(map(lambda country: country["gold"] + country["silver"] + country["bronze"], medals))

# 2. Używamy map(), aby uzyskać listę nazw krajów
countries = list(map(lambda country: country["country"], medals))

# 3. Tworzymy wykres słupkowy
plt.bar(countries, total_medals, color='blue')  # Tworzymy słupki dla krajów i ich liczby medali

# 4. Dodajemy tytuł wykresu oraz etykiety osi
plt.title('Total Medals Won by Each Country')  # Tytuł wykresu
plt.xlabel('Countries')  # Etykieta osi X (kraje)
plt.ylabel('Total Medals')  # Etykieta osi Y (liczba medali)

# 5. Wyświetlamy wykres
plt.show()
