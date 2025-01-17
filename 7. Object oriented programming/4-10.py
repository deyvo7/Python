class Points:
    """
    Klasa Points reprezentuje zbiór punktów na płaszczyźnie kartezjańskiej.
    Przechowuje współrzędne punktów jako tablicę dwuwymiarową.
    """

    def __init__(self, coordinates):
        """
        Konstruktor klasy Points.
        - coordinates: Lista współrzędnych punktów w formacie [[x1, y1], [x2, y2], ...].
        """
        self.coordinates = coordinates  # Przechowujemy współrzędne w obiekcie

    def m(self, n):
        """
        Metoda sprawdzająca, czy co najmniej n punktów znajduje się w I ćwiartce układu współrzędnych.
        Punkt jest w I ćwiartce, gdy jego współrzędne x > 0 i y > 0.
        - n: Liczba punktów do sprawdzenia.
        Zwraca:
        - True, jeśli co najmniej n punktów znajduje się w I ćwiartce.
        - False, w przeciwnym razie.
        """
        count = 0  # Licznik punktów w I ćwiartce
        for x, y in self.coordinates:
            if x > 0 and y > 0:  # Sprawdzamy, czy punkt znajduje się w I ćwiartce
                count += 1  # Zwiększamy licznik
                if count >= n:  # Jeśli osiągnęliśmy wymaganą liczbę punktów, kończymy
                    return True
        return False  # Jeśli nie znaleziono wystarczającej liczby punktów, zwracamy False


# Przykłady użycia
points = Points([[2, 3], [1, 8], [-6, 4], [3, -7]])

# Sprawdzamy, czy co najmniej 2 punkty są w I ćwiartce
print(points.m(2))  # Wynik: True

# Sprawdzamy, czy co najmniej 3 punkty są w I ćwiartce
print(points.m(3))  # Wynik: False
