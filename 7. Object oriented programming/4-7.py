class Statistics:
    # Konstruktor klasy Statistics
    def __init__(self):
        # Tworzymy pustą listę, aby przechowywać liczby
        self.numbers = []

    def add_number(self, number):
        """
        Funkcja do dodawania nowej liczby do zbioru.
        - `number`: liczba, którą chcemy dodać.
        """
        self.numbers.append(number)  # Dodajemy liczbę do listy

    def display_numbers(self):
        """
        Funkcja do wyświetlania wszystkich liczb w zbiorze.
        Liczby są wyświetlane w jednej linii, oddzielone spacją.
        """
        if self.numbers:  # Sprawdzamy, czy lista nie jest pusta
            print("Liczby w zbiorze:", " ".join(map(str, self.numbers)))
        else:
            print("Zbiór liczb jest pusty!")  # Informacja, gdy lista jest pusta

    def get_maximum(self):
        """
        Funkcja zwraca największą liczbę w zbiorze.
        Zwraca None, jeśli zbiór jest pusty.
        """
        if self.numbers:  # Sprawdzamy, czy lista nie jest pusta
            return max(self.numbers)  # Używamy funkcji max, aby znaleźć największą liczbę
        else:
            return None  # Gdy lista jest pusta, zwracamy None

    def get_minimum(self):
        """
        Funkcja zwraca najmniejszą liczbę w zbiorze.
        Zwraca None, jeśli zbiór jest pusty.
        """
        if self.numbers:  # Sprawdzamy, czy lista nie jest pusta
            return min(self.numbers)  # Używamy funkcji min, aby znaleźć najmniejszą liczbę
        else:
            return None  # Gdy lista jest pusta, zwracamy None

    def get_mean(self):
        """
        Funkcja oblicza średnią arytmetyczną liczb w zbiorze.
        Zwraca None, jeśli zbiór jest pusty.
        """
        if self.numbers:  # Sprawdzamy, czy lista nie jest pusta
            return sum(self.numbers) / len(self.numbers)  # Sumujemy liczby i dzielimy przez ich ilość
        else:
            return None  # Gdy lista jest pusta, zwracamy None

    def get_median(self):
        """
        Funkcja oblicza medianę liczb w zbiorze.
        Mediana to środkowa wartość po posortowaniu zbioru.
        Zwraca None, jeśli zbiór jest pusty.
        """
        if self.numbers:  # Sprawdzamy, czy lista nie jest pusta
            sorted_numbers = sorted(self.numbers)  # Sortujemy liczby
            n = len(sorted_numbers)  # Liczba elementów w liście
            middle = n // 2  # Indeks środkowy

            if n % 2 == 0:  # Jeśli liczba elementów jest parzysta
                # Mediana to średnia dwóch środkowych liczb
                return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
            else:
                # Jeśli liczba elementów jest nieparzysta, mediana to środkowa liczba
                return sorted_numbers[middle]
        else:
            return None  # Gdy lista jest pusta, zwracamy None

    def display_statistics(self):
        """
        Funkcja wyświetla wszystkie obliczone/statystyczne wartości:
        - Najmniejszą liczbę
        - Największą liczbę
        - Średnią arytmetyczną
        - Medianę
        """
        print("Statystyki zbioru liczb:")
        print("Najmniejsza liczba:", self.get_minimum())
        print("Największa liczba:", self.get_maximum())
        print("Średnia arytmetyczna:", self.get_mean())
        print("Mediana:", self.get_median())


# ----------------------------
# Główna część programu
# ----------------------------

# Tworzymy obiekt klasy Statistics
stats = Statistics()

# Dodajemy liczby do zbioru (zgodnie z poleceniem)
numbers_to_add = [12, 37, 6, 9, 17]  # Liczby do dodania
for num in numbers_to_add:
    stats.add_number(num)  # Dodajemy każdą liczbę do obiektu stats

# Wyświetlamy liczby w zbiorze
stats.display_numbers()

# Wyświetlamy statystyki
stats.display_statistics()
