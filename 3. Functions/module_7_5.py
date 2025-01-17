# Funkcja sprawdzająca, czy liczba znajduje się w podanym zakresie
def is_within_range(number, x, y):
    # Sprawdza, czy liczba jest w zakresie <x, y> (włącznie)
    return x <= number <= y
