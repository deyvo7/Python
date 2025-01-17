# Klasa opisująca przejazd taksówką
class TaxiRide:
    def __init__(self, rate_per_km):
        # Inicjalizacja obiektu z wartością stawki za kilometr
        self.rate_per_km = rate_per_km  # wartość w euro (np. 2€)
        self.distance = 0  # Początkowa odległość wynosi 0
        self.fare = 0      # Początkowa cena wynosi 0

    def calculate_fare(self, distance):
        # Metoda obliczająca cenę przejazdu na podstawie odległości
        self.distance = distance  # Przypisanie odległości
        self.fare = self.distance * self.rate_per_km  # Obliczenie opłaty (odległość * stawka za km)
    
    def print_receipt(self):
        # Metoda drukująca paragon z informacjami o przejeździe
        print(f"Distance: {self.distance} km, Rate: {self.rate_per_km} €/km, Fare: {self.fare} €")


def main():
    # Tworzenie obiektów reprezentujących dwa przejazdy taksówkowe
    # Pobieranie stawek za kilometr z wejścia użytkownika
    taxi1 = TaxiRide(int(input("Rate per km of taxi1: ")))  
    taxi2 = TaxiRide(int(input("Rate per km of taxi2: ")))  
    
    # Pobieranie odległości dla obu przejazdów
    taxi1.calculate_fare(int(input("Distance of taxi1 in km: ")))
    taxi2.calculate_fare(int(input("Distance of taxi2 in km: ")))
    
    # Drukowanie paragonów dla obu przejazdów
    taxi1.print_receipt()
    taxi2.print_receipt()

# Uruchomienie głównej funkcji programu
if __name__ == "__main__":
    main()
