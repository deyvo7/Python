# Funkcja konwertująca prędkość z metrów na sekundę (m/s) na kilometry na godzinę (km/h)
def ms_to_kmh(ms):
    # Aby przeliczyć m/s na km/h, mnożymy przez 3.6
    return ms * 3.6

# Pobieramy wartość prędkości w metrach na sekundę od użytkownika
# Funkcja input() zwraca dane jako tekst, więc konwertujemy je na liczbę zmiennoprzecinkową (float)
ms = float(input("m/s: "))

# Wywołujemy funkcję ms_to_kmh() i wypisujemy wynik
# f-string pozwala na wstawienie wartości zmiennych do tekstu
# Wypisujemy wynik przeliczenia prędkości z m/s na km/h
print(f"{ms} m/s = {ms_to_kmh(ms)} km/h")
