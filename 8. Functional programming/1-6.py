# Definiujemy anonimową funkcję (lambda), która oblicza średnią prędkość pojazdu
# Funkcja lambda przyjmuje trzy argumenty: distance (dystans w km), hours (godziny) i minutes (minuty)
# Funkcja zwraca wynik obliczenia średniej prędkości, gdzie czas w minutach przekonwertowany jest na godziny
avg_speed = lambda x, y, z: x / (y + (z / 60))

# Pobieramy dane wejściowe od użytkownika
# Funkcja input() zwraca dane jako tekst, więc zamieniamy je na liczby zmiennoprzecinkowe (float)
distance = float(input("Enter distance in km: "))  # Dystans w kilometrach
hours = float(input("Enter number of travel hours: "))  # Liczba godzin podróży
minutes = float(input("Enter number of travel minutes: "))  # Liczba minut podróży

# Wywołujemy funkcję avg_speed() z argumentami: distance, hours, minutes
# Funkcja round() zaokrągla wynik do jednej cyfry po przecinku
# Wypisujemy wynik obliczenia średniej prędkości
print(f"Average speed: {round(avg_speed(distance, hours, minutes), 1)} km/h")
