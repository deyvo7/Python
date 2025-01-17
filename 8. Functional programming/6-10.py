import matplotlib.pyplot as plt

# Słownik z miastami i odpowiadającymi im temperaturami
temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Używamy map(), aby wyodrębnić dwie listy:
# Pierwsza lista: nazwy miast
# Druga lista: odpowiadające im temperatury
cities = list(map(lambda x: x[0], temperatures.items()))  # Lista miast
temps = list(map(lambda x: x[1], temperatures.items()))  # Lista temperatur

# Tworzymy wykres słupkowy
plt.bar(cities, temps, color='blue')

# Dodajemy tytuł wykresu oraz opisy osi
plt.title('Temperatures Recorded in Cities')
plt.xlabel('Cities')
plt.ylabel('Temperature (°C)')

# Wyświetlamy wykres
plt.show()
