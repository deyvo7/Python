# Funkcja obliczająca średnią prędkość pojazdu
# Funkcja przyjmuje trzy argumenty: distance (dystans w km), hours (godziny) i minutes (minuty)
# Średnia prędkość obliczana jest jako dystans podzielony przez całkowity czas podróży (w godzinach)
def avg_speed(distance, hours, minutes):
    # Całkowity czas podróży w godzinach obliczamy dodając minuty przekonwertowane na godziny
    # minuty dzielimy przez 60, ponieważ 1 godzina ma 60 minut
    return distance / (hours + minutes / 60)

# Pobieramy dane wejściowe od użytkownika
# Funkcja input() zwraca dane jako tekst, więc zamieniamy je na liczby zmiennoprzecinkowe (float)
distance = float(input("Enter distance in km: "))  # Dystans w kilometrach
hours = float(input("Enter number of travel hours: "))  # Liczba godzin podróży
minutes = float(input("Enter number of travel minutes: "))  # Liczba minut podróży

# Obliczamy średnią prędkość, wywołując funkcję avg_speed() i przekazując odpowiednie argumenty
# Funkcja round() zaokrągla wynik do jednej cyfry po przecinku
print(f"Average speed: {round(avg_speed(distance, hours, minutes), 1)} km/h")
