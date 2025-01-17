class Stadium:
    """
    Klasa Stadium reprezentuje stadion z sektorami i liczbą kibiców w każdym sektorze.
    """

    def __init__(self, sectors):
        """
        Konstruktor klasy Stadium.
        - sectors: Słownik, gdzie klucz to sektor (litera), a wartość to liczba kibiców.
        """
        self.sectors = sectors  # Przechowujemy dane sektorów w obiekcie

    def m1(self, s, n):
        """
        Metoda m1 pozwala zmienić liczbę kibiców w sektorze lub dodać nowy sektor.
        - s: Sektor (litera, np. "A").
        - n: Liczba kibiców (int).
        """
        self.sectors[s] = n  # Dodanie lub aktualizacja liczby kibiców w sektorze

    def m2(self, s):
        """
        Metoda m2 zwraca sumę kibiców z sektorów podanych w ciągu znaków.
        - s: Ciąg znaków reprezentujących sektory (np. "GD").
        Zwraca:
        - Suma kibiców w podanych sektorach (int).
        """
        total = 0  # Inicjalizujemy sumę kibiców
        for sector in s:
            # Sprawdzamy, czy sektor istnieje w danych
            if sector in self.sectors:
                total += self.sectors[sector]  # Dodajemy liczbę kibiców z danego sektora
        return total


# Przykłady użycia
stadium = Stadium({"A": 120, "D": 150, "G": 90, "K": 110})

# Aktualizujemy liczbę kibiców w sektorze "G"
stadium.m1("G", 130)

# Obliczamy sumę kibiców w sektorach "G" i "D"
print(stadium.m2("GD"))  # Wynik: 280

# Obliczamy sumę kibiców w sektorach "K", "E" i "J"
# Sektory "E" i "J" nie istnieją, więc są pomijane
print(stadium.m2("KEJ"))  # Wynik: 110
