# Definicja pojemności butelki i tolerancji
bottle_capacity = 500  # Pojemność butelki w ml
tolerance = 0.02  # Tolerancja 2%

# Lista wyników napełniania butelek
filled_bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

# Funkcja, która sprawdza, czy butelka jest niewłaściwie napełniona
# Przyjmuje wartość napełnienia butelki jako argument
# Zwraca True, jeśli wartość jest poza dozwolonym zakresem, False w przeciwnym przypadku
def is_incorrect(filling):
    min_allowed = bottle_capacity - (bottle_capacity * tolerance)  # Minimalna dozwolona wartość (98% pojemności)
    max_allowed = bottle_capacity + (bottle_capacity * tolerance)  # Maksymalna dozwolona wartość (102% pojemności)
    return filling < min_allowed or filling > max_allowed  # Zwraca True, jeśli poza zakresem

# Użycie funkcji filter() z funkcją anonimową, aby wybrać butelki niewłaściwie napełnione
incorrect_bottles = list(filter(lambda x: is_incorrect(x), filled_bottles))

# Obliczanie procentu niewłaściwie napełnionych butelek
incorrect_percentage = (len(incorrect_bottles) / len(filled_bottles)) * 100

# Wyświetlanie wyników
print(f"Bottle capacity:    {bottle_capacity}ml")
print(f"Filling tolerance:  {tolerance * 100}%")
print(f"Filled bottles:     {', '.join(map(str, filled_bottles))}")
print(f"Incorrectly filled: {incorrect_percentage:.0f}%")
