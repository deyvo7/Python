# Definiujemy anonimową funkcję (lambda), która konwertuje prędkość z m/s na km/h
# Funkcja lambda przyjmuje jeden argument ms (prędkość w m/s) i mnoży go przez 3.6
ms_to_kmh = lambda ms: ms * 3.6

# Pobieramy wartość prędkości w metrach na sekundę od użytkownika
# Funkcja input() zwraca dane jako tekst, dlatego zamieniamy je na liczbę zmiennoprzecinkową (float)
ms = float(input("m/s: "))

# Wywołujemy anonimową funkcję ms_to_kmh() i wypisujemy wynik
# f-string pozwala na wstawienie wartości zmiennych do tekstu
# Wypisujemy wynik przeliczenia prędkości z m/s na km/h
print(f"{ms} m/s = {ms_to_kmh(ms)} km/h")
