import csv  # Importujemy bibliotekę do pracy z plikami CSV

# Funkcja, która wczytuje dane z pliku CSV o województwach
def load_provinces(file_name):
    provinces = {}  # Tworzymy pusty słownik, który będzie przechowywał dane o województwach
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)  # Używamy csv.reader do wczytania danych z pliku
        next(reader)  # Pomijamy pierwszą linię, ponieważ zawiera ona nagłówki (np. "Letter, Name")
        for row in reader:  # Iterujemy po każdej kolejnej linii w pliku
            letter, name = row  # Każda linia zawiera dwie kolumny: literę i nazwę województwa
            provinces[letter] = name  # Dodajemy literę jako klucz, a nazwę województwa jako wartość
    return provinces  # Zwracamy słownik województw

# Funkcja wczytująca numery rejestracyjne z pliku tekstowego
def load_vehicle_numbers(file_name):
    vehicle_numbers = []  # Tworzymy pustą listę, która przechowa numery rejestracyjne pojazdów
    with open(file_name, mode='r', encoding='utf-8') as file:
        for line in file:  # Czytamy każdą linię z pliku
            vehicle_numbers.append(line.strip())  # Usuwamy zbędne białe znaki na początku i końcu linii i dodajemy numer do listy
    return vehicle_numbers  # Zwracamy listę numerów rejestracyjnych

# Funkcja, która liczy liczbę pojazdów w każdym województwie
def count_vehicles_by_province(vehicle_numbers, provinces):
    vehicle_counts = {province: 0 for province in provinces.values()}  # Tworzymy słownik, w którym dla każdego województwa zaczynamy od liczby 0

    for vehicle in vehicle_numbers:  # Iterujemy po każdym numerze rejestracyjnym
        first_letter = vehicle[0]  # Pierwsza litera numeru rejestracyjnego odpowiada województwu
        if first_letter in provinces:  # Jeśli ta litera jest w słowniku województw
            province = provinces[first_letter]  # Pobieramy nazwę województwa na podstawie litery
            vehicle_counts[province] += 1  # Zwiększamy licznik pojazdów dla danego województwa

    return vehicle_counts  # Zwracamy słownik, w którym dla każdego województwa mamy liczbę pojazdów

# Funkcja główna, która uruchamia program
def main():
    provinces = load_provinces('province.csv')  # Wczytujemy dane o województwach z pliku
    vehicle_numbers = load_vehicle_numbers('vehicle.txt')  # Wczytujemy numery rejestracyjne pojazdów z pliku

    # Zliczamy pojazdy w każdym województwie
    vehicle_counts = count_vehicles_by_province(vehicle_numbers, provinces)

    # Wyświetlamy liczbę pojazdów w każdym województwie
    for province, count in vehicle_counts.items():
        print(f"W województwie {province} zarejestrowanych jest {count} pojazdów.")

# Uruchamiamy funkcję główną
if __name__ == '__main__':
    main()
